# Study Session Tracker API

A REST API built with FastAPI to track study sessions, subjects, productivity, and learning performance.

## Features

* Study session management
* Subject tracking
* SQLite database integration
* Request validation with Pydantic
* Modular API architecture
* Service layer separation

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn

## Project Structure

```text id="st1"
api/
├── models/
├── routes/
├── schemas/
├── services/
└── database.py

src/
└── main.py
```

## Purpose

This project was built to practice:

* Backend development
* REST APIs
* CRUD operations
* SQLAlchemy ORM
* Database integration
* API architecture
* Request validation
* Service layer separation
* Learning analytics systems

## How to Run

Create and activate a virtual environment:

```bash id="st2"
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash id="st3"
pip install -r requirements.txt
```

Run the server:

```bash id="st4"
python main.py
```

## API Documentation

Swagger UI:

```text id="st5"
http://127.0.0.1:8000/docs
```

ReDoc:

```text id="st6"
http://127.0.0.1:8000/redoc
```
