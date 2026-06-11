from fastapi import APIRouter, HTTPException
from datetime import date
from typing import Optional
from api.database import SessionLocal
from api.models.study_session import StudySession
from api.schemas.study_session import PostSession, PutSession
from api.services.study_session import get_sessions, create_session, update_study_session, delete_study_session

session_router = APIRouter(prefix="/api/sessions", tags=["StudySession"])

@session_router.get("/")
def all_sessions(selected_date: Optional[date] = None):
    
    db = SessionLocal()

    try:
        return get_sessions(db, selected_date)
    
    finally:
        db.close()


@session_router.post("/")
def post_session(session: PostSession):
    
    db = SessionLocal()

    try:
        return create_session(db, session)

    finally:
        db.close()


@session_router.put("/{session_id}")
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