from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Dict

app = FastAPI(title="Flames Admin Auth API", version="1.0.0")

# CORS setup - allow frontend dev server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ForgotRequest(BaseModel):
    email: EmailStr


@app.get("/health")
async def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/auth/forgot")
async def forgot_password(payload: ForgotRequest) -> Dict[str, str]:
    # In a real app, you'd generate a token and send email here.
    # We return a generic response for security best practice.
    return {
        "message": "If that email exists in our system, we've sent a password reset link.",
        "email": payload.email,
    }
