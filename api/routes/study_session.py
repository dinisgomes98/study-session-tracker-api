from fastapi import APIRouter
from datetime import date
from typing import Optional
from api.database import SessionLocal
from api.schemas.study_session import PostSession, PutSession, StudySessionResponse
from api.services.study_session import get_sessions, create_session, update_study_session, delete_study_session

session_router = APIRouter(prefix="/api/sessions", tags=["StudySession"])

@session_router.get("/", response_model=list[StudySessionResponse])
def all_sessions(selected_date: Optional[date] = None):
    
    db = SessionLocal()

    try:
        return get_sessions(db, selected_date)
    
    finally:
        db.close()


@session_router.post("/", response_model=StudySessionResponse)
def post_session(session: PostSession):
    
    db = SessionLocal()

    try:
        return create_session(db, session)

    finally:
        db.close()


@session_router.put("/{session_id}", response_model=StudySessionResponse)
def update_session(session_id: int, session: PutSession):
    
    db = SessionLocal()

    try:
        return update_study_session(db, session_id, session)
    
    finally:
        db.close()


@session_router.delete("/{session_id}")
def delete_session(session_id: int):
    
    db = SessionLocal()
    
    try:
        return delete_study_session(db, session_id)

    finally:
        db.close()