# Study Session Tracker API

A REST API built with FastAPI to track study sessions, subjects, productivity, and learning performance.

## Features

- Full CRUD operations for study sessions
- Full CRUD operations for subjects
- Subject-to-session relationships
- SQLite database integration
- Request validation with Pydantic
- Modular API architecture
- Service layer separation
- Study session filtering by date
- Study analytics and statistics
- Subject-specific statistics
- Weekly and monthly performance analysis

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## Project Structure

```text
api/
├── models/
│   ├── study_session.py
│   └── subject.py
├── routes/
│   ├── study_session.py
│   └── subject.py
├── schemas/
│   ├── study_session.py
│   └── subject.py
├── services/
│   ├── study_session.py
│   └── subject.py
└── database.py

src/
└── main.py
```

## Purpose

This project was built to practice:

- Backend development
- REST APIs
- CRUD operations
- SQLAlchemy ORM
- Database relationships
- Query filtering
- Aggregation queries
- Analytics endpoints
- Database integration
- API architecture
- Request validation
- Service layer separation
- Learning analytics systems

## How to Run

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the server:

```bash
python main.py
```

## API Documentation

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

## Available Endpoints

### Study Sessions

- GET `/api/sessions`
- POST `/api/sessions`
- PUT `/api/sessions/{session_id}`
- DELETE `/api/sessions/{session_id}`
- GET `/api/sessions?selected_date=YYYY-MM-DD`
- GET `/api/sessions/stats`
- GET `/api/sessions/stats?selected_week=XX&selected_year=YYYY`
- GET `/api/sessions/stats?selected_month=XX&selected_year=YYYY`

### Subjects

- GET `/api/subjects`
- POST `/api/subjects`
- PUT `/api/subjects/{subject_id}`
- DELETE `/api/subjects/{subject_id}`
- GET `/api/subjects/{subject_id}/stats`

## Analytics

The API provides learning analytics such as:

- Total study sessions
- Total study time
- Most studied subject
- Number of sessions per subject
- Average productivity score
- Weekly statistics
- Monthly statistics
- Subject-specific performance metrics