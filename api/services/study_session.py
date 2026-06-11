from fastapi import HTTPException
from api.models.subject import Subject
from api.models.study_session import StudySession

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