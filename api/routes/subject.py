from fastapi import APIRouter
from api.database import SessionLocal
from api.schemas.subject import SubjectResponse, PostSubject, PutSubject
from api.services.subject import get_subjects, create_subject, update_subject, delete_subject, stats_by_subject

subject_router = APIRouter(prefix="/api/subjects", tags=["Subject"])

@subject_router.get("/", response_model=list[SubjectResponse])
def all_subjects():
    
    db = SessionLocal()

    try:
        return get_subjects(db)
    
    finally:
        db.close()


@subject_router.post("/", response_model=SubjectResponse)
def post_subject(subject: PostSubject):
    
    db = SessionLocal()

    try:
        return create_subject(db, subject)

    finally:
        db.close()


@subject_router.put("/{subject_id}", response_model=SubjectResponse)
def update_subject_route(subject_id: int, subject: PutSubject):
    
    db = SessionLocal()

    try:
        return update_subject(db, subject_id, subject)
    
    finally:
        db.close()


@subject_router.delete("/{subject_id}")
def delete_subject_route(subject_id: int):
    
    db = SessionLocal()
    
    try:
        return delete_subject(db, subject_id)

    finally:
        db.close()


@subject_router.get("/{subject_id}/stats")
def stats_subject(subject_id: int):
    
    db = SessionLocal()
    
    try:
        return stats_by_subject(db, subject_id)
    
    finally:
        db.close()