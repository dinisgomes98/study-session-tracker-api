from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.database import Base


class Subject(Base):
    __tablename__ = "subjects"

    id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, nullable=False)

    sessions = relationship("StudySession", back_populates="subject")
