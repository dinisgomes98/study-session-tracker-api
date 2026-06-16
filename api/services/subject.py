from fastapi import HTTPException
from api.models.subject import Subject
from api.models.study_session import StudySession
from sqlalchemy import func

def get_subjects(db):
    return db.query(Subject).all()


def create_subject(db, subject):

    existing_subject = db.query(Subject).filter(Subject.subject_name == subject.subject_name).first()
    
    if existing_subject is not None:
        raise HTTPException(
            status_code=409,
            detail="Subject already exists"
        )
        
   
    new_subject = Subject(
        subject_name = subject.subject_name
    )

    db.add(new_subject)
    db.commit()
    db.refresh(new_subject)

    return new_subject


def update_subject(db, subject_id, subject):
    existing_subject = db.query(Subject).filter(Subject.id == subject_id).first()
    
    if existing_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")

    if subject.subject_name is not None:
        existing_subject.subject_name = subject.subject_name

    db.commit()
    db.refresh(existing_subject)

    return existing_subject


def delete_subject(db, subject_id):
    existing_subject = db.query(Subject).filter(Subject.id == subject_id).first()

    if existing_subject is None:
        raise HTTPException(status_code=404, detail="Subject not found")
    

    db.delete(existing_subject)
    db.commit()

    return {"message": "Subject deleted successfully"}

def stats_by_subject(db, subject_id):

    subject = db.query(Subject).filter(Subject.id == subject_id).first()

    if subject is None:
        raise HTTPException(
            status_code=404,
            detail="Subject not found"
        )

    total_sessions = (
        db.query(StudySession)
        .filter(Subject.subject_id_id == subject_id)
        .count()
    )

    total_time =  (
        db.query(
            func.sum(StudySession.time_spent)
        )
        .filter(StudySession.subject_id == subject_id)
        .scalar()
    )

    avg_productivity = (
        db.query(
            func.avg(StudySession.productivity)
        )
        .filter(StudySession.subject_id == subject_id)
        .scalar()
    )

    return {
        "subject": subject.subject_name,
        "total_sessions": total_sessions,
        "total_time": round(total_time or 0, 2),
        "average_productivity": round(avg_productivity or 0, 2)
    }