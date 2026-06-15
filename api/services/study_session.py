from fastapi import HTTPException
from api.models.subject import Subject
from api.models.study_session import StudySession
from sqlalchemy import func

def get_sessions(db, selected_date):
    query = db.query(StudySession)

    if selected_date is not None:
        query = query.filter(StudySession.date == selected_date)

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

def stats_study_sessions(db):

    total_sessions = db.query(StudySession).count()

    time_spent = db.query(func.sum(StudySession.time_spent)).scalar()

    most_studied_subject = (
        db.query(
            Subject.subject_name,
            func.count(StudySession.id).label("total")
        )
        .join(StudySession)
        .group_by(Subject.id)
        .order_by(func.count(StudySession.id).desc())
        .first()
    )

    avg_productivity = db.query(func.avg(StudySession.productivity)).scalar()

    return {
        "total_sessions": total_sessions,
        "total_time_spent": round(time_spent or 0, 2),
        "most_studied_": most_studied_subject[0] if most_studied_subject else None,
        "most_studied_subject": most_studied_subject[0] if most_studied_subject else None,
        "average_session_productivity": round(avg_productivity or 0, 2)
    }