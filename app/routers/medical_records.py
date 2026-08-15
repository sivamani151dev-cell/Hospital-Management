from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.medical_record import MedicalRecord
from app.models.user import User
from app.schemas.medical_record import MedicalRecordCreate, MedicalRecordResponse
from app.auth import decode_access_token
from fastapi.security import OAuth2PasswordBearer
import logging

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/medical-records", tags=["Medical Records"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    username = decode_access_token(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    user = db.query(User).filter(User.username == username).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    return user

@router.post("/", response_model=MedicalRecordResponse, status_code=201)
def create_record(record: MedicalRecordCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_record = MedicalRecord(
        diagnosis=record.diagnosis,
        prescription=record.prescription,
        notes=record.notes,
        patient_id=record.patient_id,
        doctor_id=record.doctor_id
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/patient/{patient_id}", response_model=list[MedicalRecordResponse])
def get_patient_records(patient_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(MedicalRecord).filter(MedicalRecord.patient_id == patient_id).all()