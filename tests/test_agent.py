from fastapi.testclient import TestClient
from backend.main import app
import json

client = TestClient(app)

def test_availability_and_booking_flow():
    date = "2025-11-19"
    r = client.get("/api/calendly/availability", params={"date": date, "appointment_type": "consultation"})
    assert r.status_code == 200
    data = r.json()
    assert "available_slots" in data

    # pick first available slot
    slot = next((s for s in data["available_slots"] if s["available"]), None)
    assert slot is not None

    # book
    booking_payload = {
        "appointment_type": "consultation",
        "date": date,
        "start_time": slot["start_time"],
        "patient": {"name":"Test User","email":"test@example.com","phone":"1234567890"},
        "reason":"Testing"
    }
    r2 = client.post("/api/chat/book", json=booking_payload)
    assert r2.status_code == 200
    j = r2.json()
    assert j["status"] == "confirmed"