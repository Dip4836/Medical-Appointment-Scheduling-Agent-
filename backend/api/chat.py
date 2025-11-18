from fastapi import APIRouter, HTTPException
from ..agent.scheduling_agent import suggest_slots, build_booking_payload, answer_faq
from ..models.schemas import BookingRequest
from fastapi import Body
from ..tools.booking_tool import book as booking_call

router = APIRouter(prefix="/api/chat", tags=["chat"])

@router.get("/suggest")
def suggest(date: str, appointment_type: str = "consultation"):
    """
    Returns a set of suggested slots for a date and type.
    """
    try:
        slots = suggest_slots(date, appointment_type)
        return {"date": date, "suggested_slots": slots}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/book", summary="Book an appointment via Calendly mock")
def book_endpoint(body: BookingRequest):
    payload = build_booking_payload(body)
    # call booking tool (calls mock calendly endpoint)
    res = booking_call(payload)
    return res

@router.post("/faq")
def faq_endpoint(query: dict = Body(...)):
    q = query.get("q")
    if not q:
        raise HTTPException(status_code=400, detail="Provide 'q' in body")
    return answer_faq(q)