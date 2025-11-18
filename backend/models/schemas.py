from pydantic import BaseModel, EmailStr
from typing import List, Optional, Dict

class Patient(BaseModel):
    name: str
    email: EmailStr
    phone: Optional[str]

class AvailabilitySlot(BaseModel):
    start_time: str
    end_time: str
    available: bool

class AvailabilityResponse(BaseModel):
    date: str
    available_slots: List[AvailabilitySlot]

class BookingRequest(BaseModel):
    appointment_type: str
    date: str
    start_time: str
    patient: Patient
    reason: Optional[str]

class BookingResponse(BaseModel):
    booking_id: str
    status: str
    confirmation_code: str
    details: Dict