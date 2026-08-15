from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class MedicalRecordCreate(BaseModel):
    diagnosis: str
    prescription: Optional[str] = None
    notes: Optional[str] = None
    patient_id: int
    doctor_id: int

class MedicalRecordResponse(BaseModel):
    id: int
    diagnosis: str
    prescription: Optional[str]
    notes: Optional[str]
    created_at: datetime
    patient_id: int
    doctor_id: int

    class Config:
        from_attributes = True