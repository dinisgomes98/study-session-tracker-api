from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from api.database import Base

class StudySession(Base):
    __tablename__ = "study_sessions"

    id = Column(Integer, primary_key=True, index=True)
    subject_id = Column(Integer, ForeignKey("subjects.id"), nullable=False)
    date = Column(Date, nullable=False)
    time_spent = Column(Integer, nullable=False)
    productivity = Column(Integer, nullable=False)

    subject = relationship("Subject", back_populates="sessions")