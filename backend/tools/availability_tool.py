import httpx
from typing import List, Dict

CALENDLY_BASE = "http://localhost:8000/api/calendly"

def get_availability(date: str, appointment_type: str = "consultation"):
    url = f"{CALENDLY_BASE}/availability"
    r = httpx.get(url, params={"date": date, "appointment_type": appointment_type}, timeout=10)
    r.raise_for_status()
    return r.json()