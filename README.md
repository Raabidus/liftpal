# liftpal
```
backend/
├── api.py           # FastAPI routes
├── config.py        # App configuration and settings
├── crud.py          # CRUD operations
├── database.py      # Database connection setup
├── init_db.py       # Database initialization and seeding
├── models.py        # SQLAlchemy ORM models
├── schemas.py       # Pydantic models (request/response validation)
tests/
└── test_crud.py     # Unit tests for CRUD operations
```
#### Requirements
    •	Python 3.x
    •	FastAPI
    •	SQLAlchemy
    •	psycopg2 (PostgreSQL driver)
    •	Pipenv (for virtual environment & package management)

#### Installation
git clone <repo_url>
cd LiftPal
pipenv install

#### Runnig the App
pipenv run uvicorn backend.api:app --reload

#### Database Setup
pipenv run python backend/init_db.py

#### Testing
pipenv run pytest

#### API Documentation
After running the server, visit:
    •	Swagger UI: http://127.0.0.1:8000/docs
    •	ReDoc: http://127.0.0.1:8000/redoc
