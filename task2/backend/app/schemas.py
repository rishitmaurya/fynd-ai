# schemas.py
from pydantic import BaseModel
from typing import Optional

class SubmitRequest(BaseModel):
    rating: int
    review: str

class SubmissionOut(BaseModel):
    id: int
    timestamp: str
    rating: int
    review: str
    ai_reply: Optional[str]
    ai_summary: Optional[str]
    ai_actions: Optional[str]
