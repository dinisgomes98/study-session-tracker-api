from fastapi import APIRouter, Query, HTTPException
from datetime import date
from typing import Optional
from api.database import SessionLocal
from api.schemas.study_session import PostSession, PutSession, StudySessionResponse
from api.services.study_session import get_sessions, create_session, update_study_session, delete_study_session, stats_study_sessions

session_router = APIRouter(prefix="/api/sessions", tags=["StudySession"])

@session_router.get("/", response_model=list[StudySessionResponse])
def all_sessions(
        selected_date: Optional[date] = None, 
        subject_id: Optional[int] = None,
        productivity: Optional[int] = Query(None, ge=1, le=5)
):
    
    db = SessionLocal()

    try:
        return get_sessions(db, selected_date, subject_id, productivity)
    
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


@session_router.get("/stats")
def stats_sessions(
    selected_week: Optional[int] = None,
    selected_month: Optional[int] = None,
    selected_year: Optional[int] = None
):
    if selected_week is not None and not 1 <= selected_week <= 53:
        raise HTTPException(status_code=400, detail="selected_week must be between 1 and 53")

    if selected_month is not None and not 1 <= selected_month <= 12:
        raise HTTPException(status_code=400, detail="selected_month must be between 1 and 12")
    
    if selected_week is not None and selected_year is None:
        raise HTTPException(
            status_code=400,
            detail="selected_year is required when filtering by selected_week"
        )

    if selected_month is not None and selected_year is None:
        raise HTTPException(
            status_code=400,
            detail="selected_year is required when filtering by selected_month"
        )
    
    if selected_month is not None and selected_week is not None:
        raise HTTPException(
            status_code=400,
            detail="Chose either selected_week or selected_month"
        )
    
    db = SessionLocal()
    
    try:
        return stats_study_sessions(db, selected_week, selected_month, selected_year)

    finally:
        db.close()