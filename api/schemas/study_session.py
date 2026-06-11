from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class StudySessionResponse(BaseModel):
    id: int
    subject_id: int
    date: date
    time_spent: int
    productivity: int

    class Config:
        from_attributes = True

class PostSession(BaseModel):
    subject_id: int
    date: date
    time_spent: int = Field(..., gt=0)
    productivity: int = Field(..., ge=1, le=5)

class PutSession(BaseModel):
    subject_id: Optional[int] = None
    date: Optional[date] = None
    time_spent: Optional[int] = None
    productivity: Optional[int] = None

    