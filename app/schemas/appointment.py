from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.models.appointment import AppointmentStatus

class AppointmentCreate(BaseModel):
    appointment_date: datetime
    patient_id: int
    doctor_id: int
    notes: Optional[str] = None

class AppointmentUpdate(BaseModel):
    status: Optional[AppointmentStatus] = None
    notes: Optional[str] = None

class AppointmentResponse(BaseModel):
    id: int
    appointment_date: datetime
    status: AppointmentStatus
    notes: Optional[str]
    created_at: datetime
    patient_id: int
    doctor_id: int

    class Config:
        from_attributes = True