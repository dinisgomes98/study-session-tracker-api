from fastapi import FastAPI
from api.routes.study_session import session_router
from api.routes.subject import subject_router
from api.database import Base, engine
from api.models.study_session import StudySession
from api.models.subject import Subject

app = FastAPI()

app.include_router(session_router)
app.include_router(subject_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def index():
    return {"status": "study session tracker api is running"}