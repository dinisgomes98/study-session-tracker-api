from fastapi import HTTPException
from api.models.subject import Subject
from api.models.study_session import StudySession
from sqlalchemy import func
from datetime import date
from calendar import monthrange

def get_sessions(db, selected_date, subject_id, productivity):
    query = db.query(StudySession)

    if selected_date is not None:
        query = query.filter(StudySession.date == selected_date)

    if subject_id is not None:
        query = query.filter(StudySession.subject_id == subject_id)
    
    if productivity is not None:
        query = query.filter(StudySession.productivity == productivity)

    sessions = query.all()

    return sessions

def create_session(db, session):

    subject = db.query(Subject).filter(Subject.id == session.subject_id).first()
    
    if subject is None:
        raise HTTPException(
        status_code=404,
        detail="Subject not found"
    )
        
   
    new_session = StudySession(
        subject_id=session.subject_id,
        date=session.date, 
        time_spent=session.time_spent,
        productivity=session.productivity
    )

    db.add(new_session)
    db.commit()
    db.refresh(new_session)

    return new_session

def update_study_session(db, session_id, session):
    existing_session = db.query(StudySession).filter(StudySession.id == session_id).first()
    
    if existing_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
        
    if session.subject_id is not None:
        subject = db.query(Subject).filter(Subject.id == session.subject_id).first()
        
        if subject is None:
            raise HTTPException(status_code=404, detail="Subject not found")

        existing_session.subject_id = session.subject_id

    if session.date is not None:
        existing_session.date = session.date

    if session.time_spent is not None:
        existing_session.time_spent = session.time_spent

    if session.productivity is not None:
        existing_session.productivity = session.productivity

    db.commit()
    db.refresh(existing_session)

    return existing_session

def delete_study_session(db, session_id):
    existing_session = db.query(StudySession).filter(StudySession.id == session_id).first()

    if existing_session is None:
        raise HTTPException(status_code=404, detail="Session not found")
    

    db.delete(existing_session)
    db.commit()

    return {"message": "Session deleted successfully"}

def stats_study_sessions(db, selected_week, selected_month, selected_year):
    sessions_query = db.query(StudySession)
    subject_query = (
    db.query(
        Subject.subject_name,
        func.count(StudySession.id).label("total")
    )
    .join(StudySession)
)

    if selected_week is not None:
        first_week_day = date.fromisocalendar(selected_year, selected_week, 1)
        last_week_day = date.fromisocalendar(selected_year, selected_week, 7)

        sessions_query = sessions_query.filter(
            StudySession.date >= first_week_day,
            StudySession.date <= last_week_day)
        
        subject_query = subject_query.filter(
            StudySession.date >= first_week_day,
            StudySession.date <= last_week_day)

    if selected_month is not None:
        first_month_day = date(selected_year, selected_month, 1)

        last_day_number = monthrange(selected_year, selected_month)[1]

        last_month_day = date(selected_year, selected_month, last_day_number)

        sessions_query = sessions_query.filter(
            StudySession.date >= first_month_day,
            StudySession.date <= last_month_day)
        
        subject_query = subject_query.filter(
            StudySession.date >= first_month_day,
            StudySession.date <= last_month_day)

    total_sessions = sessions_query.count()

    time_spent = sessions_query.with_entities(func.sum(StudySession.time_spent)).scalar()

    most_studied_subject = (
        subject_query
        .group_by(Subject.id)
        .order_by(func.count(StudySession.id).desc())
        .first()
    )

    avg_productivity = sessions_query.with_entities(func.avg(StudySession.productivity)).scalar()

    return {
        "total_sessions": total_sessions,
        "total_time_spent": round(time_spent or 0, 2),
        "most_studied_subject": most_studied_subject[0] if most_studied_subject else None,
        "most_studied_subject_sessions": most_studied_subject[1] if most_studied_subject else 0,
        "average_session_productivity": round(avg_productivity or 0, 2)
    }