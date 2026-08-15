from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class DoctorCreate(BaseModel):
    name: str
    specialization: str
    phone: Optional[str] = None
    email: Optional[EmailStr] = None
    experience_years : Optional[int] = None

class DoctorUpdate(BaseModel):
    name: Optional[str] = None
    specialization: Optional[str] = None
    phone: Optional[str] = None
    is_available: Optional[bool] = None

class DoctorResponse(BaseModel):
    id: int
    name: str
    specialization: str
    phone: Optional[str]
    email: Optional[str]
    experience_years: Optional[int]
    is_available: bool
    created_at: datetime

    class Config:
        from_attributes = True