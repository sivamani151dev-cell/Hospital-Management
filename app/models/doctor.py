from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specializaiton = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, unique=True)
    experience_years = Column(Integer, nullable=True)
    is_available= Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    appointments = relationship("Appointment", backref="doctor")
    medical_records = relationship("MedicalRecord", backref="doctor")