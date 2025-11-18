# LiftPal

LiftPal is a work-in-progress strength training tracker. It exposes a FastAPI backend for creating users, logging workouts, and attaching individual exercises, and ships with a Quasar/Vue frontend that consumes the API. The project is structured so the backend and frontend can evolve independently while sharing a single repository.

## Tech Stack

- **Backend**: Python 3.13, FastAPI, SQLAlchemy, Pydantic, PostgreSQL, Pipenv for dependency management.
- **Frontend**: Quasar (Vue 3 + Vite), Axios for HTTP, Pinia/Vue Router scaffolding ready for future features.
- **Tooling**: Pytest (backend), ESLint + Prettier (frontend).

## Repository Layout

```
.
├── backend/              # FastAPI application
│   ├── api.py            # Route registration
│   ├── crud.py           # SQLAlchemy-based data access helpers
│   ├── database.py       # Sync SQLAlchemy engine/session factory
│   ├── models.py         # ORM models (User, Exercise, Training,…)
│   ├── schemas.py        # Pydantic request/response schemas
│   └── init_db.py        # Utility script for bootstrapping tables/data
├── frontend/             # Quasar SPA that talks to the backend
│   ├── src/boot/axios.js # Axios instance pointed at http://127.0.0.1:8000
│   └── src/services/     # API helper files (users, trainings, exercises)
├── tests/                # Pytest suite placeholders
├── Pipfile               # Backend dependencies (managed by Pipenv)
└── pytest.ini
```

## Backend

### Environment & Dependencies

1. Install Python 3.13 and Pipenv.
2. Copy `backend/config.py` and update `DATABASE_URL` to point at your PostgreSQL instance (default is `postgresql+psycopg2://martinkral:droMK139@localhost:5432/liftpal_dev`).  
   - You can also export the same DSN via `DATABASE_URL` if you refactor the config module to read from the environment.
3. Install dependencies:

```bash
pipenv install
```

### Database

Ensure PostgreSQL is running and the target database exists. Create the schema (and optionally seed demo data) with:

```bash
pipenv run python backend/init_db.py
```

### Running the API

```bash
pipenv run uvicorn backend.api:app --reload
```

- Interactive docs become available at `http://127.0.0.1:8000/docs` (Swagger UI) and `http://127.0.0.1:8000/redoc`.
- The default CORS policy (see `backend/config.py`) allows requests from the Quasar dev server (`http://localhost:9000`).

### Available Routes

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/users/` | Create a user (`username`, optional flags). |
| `GET`  | `/users/{id}` | Fetch a user by `user_id`. |
| `GET`  | `/trainings/` | List all trainings. |
| `GET`  | `/trainings/{id}` | Fetch a single training. |
| `POST` | `/trainings/` | Create a training for a user (name, type, date, note, `user_id`). |
| `POST` | `/exercises/` | Create an exercise definition (name, description, muscle group, type). |
| `GET`  | `/exercises/` | List all exercises. |
| `GET`  | `/exercises/{id}` | Fetch one exercise. |
| `POST` | `/trainings/{training_id}/exercises/?exercise_id={id}` | Attach an exercise to a training with set/rep metadata. |

> ℹ️ Several TODOs are marked in `backend/api.py`, `crud.py`, and `schemas.py` (e.g., validation gaps, optional field defaults, and richer response schemas). Consider addressing these before relying on the endpoints in production.

### Testing

The `tests/test_crud.py` file is a placeholder for future async CRUD tests. Once fixtures are fixed, run:

```bash
pipenv run pytest
```

## Frontend

The frontend is a Quasar SPA located in `frontend/`. It currently ships scaffolding (layouts, router, Pinia store) plus Axios services ready to query the backend.

### Install Dependencies

```bash
cd frontend
npm install
# or
yarn
```

### Local Development

```bash
quasar dev
```

This spins up the dev server at `http://localhost:9000` and proxies API calls through the Axios instance defined in `src/boot/axios.js` (base URL `http://127.0.0.1:8000`). Update that file if your backend runs elsewhere.

### Quality Checks & Builds

```bash
npm run lint      # ESLint
npm run format    # Prettier
quasar build      # Production bundle
```

## Recommended Workflow

1. Start PostgreSQL (`liftpal_dev` database).
2. `pipenv run uvicorn backend.api:app --reload` to start the API.
3. From `frontend/`, run `quasar dev` for the SPA.
4. Develop features in tandem, re-running tests/linters as needed.

## Future Work

- Harden validation (e.g., nullable exercise descriptions, password storage).
- Flesh out the async CRUD tests and CI workflow.
- Expand the Quasar UI beyond service stubs (forms for exercises/trainings, authentication, etc.).

Contributions and experimentation are welcome—feel free to open issues or PRs as the roadmap evolves.
