from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class SubjectResponse(BaseModel):
    id: int
    subject_name: str

    class Config:
        from_attributes = True

class PostSubject(BaseModel):
    subject_name: str = Field(..., max_length=100)
    
class PutSubject(BaseModel):
    subject_name: Optional[str] = Field(None, max_length=100)
    
    