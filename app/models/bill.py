from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, Enum, Text
from sqlalchemy.sql import func
from app.database import Base
import enum

class BillStatus(enum.Enum):
    pending = "pending"
    paid = "paid"
    cancelled = "cancelled"

class Bill(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    status = Column(Enum(BillStatus), default=BillStatus.pending)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    patient_id = Column(Integer, ForeignKey("patients.id"))