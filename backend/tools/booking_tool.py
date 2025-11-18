import httpx
from typing import Dict
CALENDLY_BASE = "http://localhost:8000/api/calendly"

def book(payload: Dict):
    url = f"{CALENDLY_BASE}/book"
    r = httpx.post(url, json=payload, timeout=10)
    r.raise_for_status()
    return r.json()