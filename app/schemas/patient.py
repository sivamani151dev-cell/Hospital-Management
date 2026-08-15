from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PatientCreate(BaseModel):
    name: str
    age: int
    blood_group: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    blood_group: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class PatientResponse(BaseModel):  
    id: int
    name: str
    age: int
    blood_group: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    created_at : datetime
    owner_id : int

    class Config:
        from_attributes = True