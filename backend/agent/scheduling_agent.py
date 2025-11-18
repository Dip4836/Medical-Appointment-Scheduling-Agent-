from ..tools.availability_tool import get_availability
from ..tools.booking_tool import book
from ..rag.faq_rag import FAQRAG
from ..models.schemas import BookingRequest
from typing import Dict, Any
import datetime
import uuid

faq = FAQRAG()

def suggest_slots(date: str, appointment_type: str):
    av = get_availability(date, appointment_type)
    # prefer available slots
    slots = [s for s in av["available_slots"] if s["available"]]
    # pick up to 5
    return slots[:5]

def build_booking_payload(booking_req: BookingRequest):
    # compute end_time from start and appointment duration
    durations = {"consultation":30, "followup":15, "physical":45, "specialist":60}
    duration = durations.get(booking_req.appointment_type, 30)
    st = datetime.datetime.strptime(booking_req.start_time, "%H:%M")
    et = (st + datetime.timedelta(minutes=duration)).time().strftime("%H:%M")
    payload = {
        "appointment_type": booking_req.appointment_type,
        "date": booking_req.date,
        "start_time": booking_req.start_time,
        "end_time": et,
        "patient": booking_req.patient.dict(),
        "reason": booking_req.reason
    }
    return payload

def answer_faq(query: str):
    return faq.get_answers(query)