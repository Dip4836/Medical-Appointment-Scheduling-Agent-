from fastapi import FastAPI
from .api import chat, calendly_integration
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(title="Appointment Scheduling Agent")

# CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(calendly_integration.router)
app.include_router(chat.router)

if __name__ == "__main__":
    port = int(os.getenv("BACKEND_PORT", 8000))
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port, reload=True)