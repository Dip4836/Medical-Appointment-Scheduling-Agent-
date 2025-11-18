from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
import uuid
import datetime
import json
import os

router = APIRouter(prefix="/api/calendly", tags=["calendly"])

DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "doctor_schedule.json")

def load_schedule():
    with open(DATA_PATH, "r") as f:
        return json.load(f)

def save_schedule(schedule):
    with open(DATA_PATH, "w") as f:
        json.dump(schedule, f, indent=2)

@router.get("/availability", response_model=Dict)
def get_availability(date: str, appointment_type: str = "consultation"):
    """
    Returns an availability JSON for the date.
    This is a simplified mock: we return every 30 minutes between 09:00-17:00 minus existing appointments.
    """
    # very simple scheduler: fixed durations per type
    durations = {
        "consultation": 30,
        "followup": 15,
        "physical": 45,
        "specialist": 60
    }
    duration = durations.get(appointment_type, 30)
    # create slots
    def parse_time(t): return datetime.datetime.strptime(t, "%H:%M").time()
    work_start = datetime.time(9, 0)
    work_end = datetime.time(17, 0)
    slots = []
    cur = datetime.datetime.strptime(date + " " + work_start.strftime("%H:%M"), "%Y-%m-%d %H:%M")
    end_dt = datetime.datetime.strptime(date + " " + work_end.strftime("%H:%M"), "%Y-%m-%d %H:%M")
    # load existing appointments for simpler collision
    schedule = load_schedule()
    taken = []
    for doc in schedule["doctors"]:
        for appt in doc.get("appointments", []):
            if appt["date"] == date:
                taken.append((appt["start"], appt["end"]))
    while cur + datetime.timedelta(minutes=duration) <= end_dt:
        s = cur.time().strftime("%H:%M")
        e = (cur + datetime.timedelta(minutes=duration)).time().strftime("%H:%M")
        # check collision
        overlapping = any(not (e <= t[0] or s >= t[1]) for t in taken)
        slots.append({"start_time": s, "end_time": e, "available": not overlapping})
        cur += datetime.timedelta(minutes=30)
    return {"date": date, "available_slots": slots}

@router.post("/book", response_model=Dict)
def book_appointment(body: Dict):
    # minimal validation and add to first doctor
    schedule = load_schedule()
    doctor = schedule["doctors"][0]
    # ensure not double-booked
    for appt in doctor.get("appointments", []):
        if appt["date"] == body["date"] and appt["start"] == body["start_time"]:
            raise HTTPException(status_code=400, detail="Slot already booked")
    # create booking id
    booking_id = f"APPT-{uuid.uuid4().hex[:8]}"
    confirmation_code = uuid.uuid4().hex[:6].upper()
    doctor.setdefault("appointments", []).append({
        "date": body["date"],
        "start": body["start_time"],
        "end": body["end_time"]
    })
    save_schedule(schedule)
    return {
        "booking_id": booking_id,
        "status": "confirmed",
        "confirmation_code": confirmation_code,
        "details": {
            "doctor": doctor["name"],
            "date": body["date"],
            "start": body["start_time"],
            "end": body["end_time"],
            "patient": body.get("patient", {})
        }
    }