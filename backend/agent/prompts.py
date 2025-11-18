# small prompt templates (if using LLM)
SLOT_SUGGESTION = """
You are an intelligent scheduling assistant.
User preference: {preference}
Appointment type: {appointment_type}
Available slots: {slots}
Recommend 3 best slots and explain why (brief).
"""