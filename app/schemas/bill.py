from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.bill import BillStatus

class BillCreate(BaseModel):
    amount: float
    description: Optional[str] = None
    patient_id: int

class BillUpdate(BaseModel):
    status: Optional[BillStatus] = None
    amount: Optional[float] = None

class BillResponse(BaseModel):
    id: int
    amount: float
    status: BillStatus
    description: Optional[str]
    created_at: datetime
    patient_id: int

    class Config:
        from_attributes = True