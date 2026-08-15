from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.bill import Bill
from app.models.user import User
from app.schemas.bill import BillCreate, BillUpdate, BillResponse
from app.auth import decode_access_token
from fastapi.security import OAuth2PasswordBearer
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/bills", tags=["Bills"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = decode_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/", response_model=BillResponse, status_code=201)
def create_bill(bill: BillCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_bill = Bill(
        amount=bill.amount,
        description=bill.description,
        patient_id=bill.patient_id
    )
    db.add(new_bill)
    db.commit()
    db.refresh(new_bill)
    return new_bill

@router.get("/patient/{patient_id}", response_model=list[BillResponse])
def get_patient_bills(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Bill).filter(Bill.patient_id == patient_id).all()

@router.put("/{bill_id}", response_model=BillResponse)
def update_bill(bill_id: int, update: BillUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    bill = db.query(Bill).filter(Bill.id == bill_id).first()
    if not bill:
        raise HTTPException(status_code=404, detail="Bill not found")
    if update.status is not None:
        bill.status = update.status
    if update.amount is not None:
        bill.amount = update.amount
    db.commit()
    db.refresh(bill)
    return bill