# BookCrust API

BookCrust is a backend project for a book-review platform. I built it to demonstrate production-style API design with authentication, role-based access control, async database access, background jobs, and Dockerized deployment.

This repository is a strong representation of how I structure backend services end to end: clean modules, migrations, containerized local development, and automated tests.

## Why I Built This

- Practice building a complete backend beyond basic CRUD.
- Apply real-world backend patterns: JWT auth, async Postgres, Redis, and task queues.

## Core Features

- User signup, login, token refresh, logout, and email verification flows.
- Password reset request and confirmation flow.
- Book management APIs with ownership checks.
- Review and tag modules for richer domain modeling.
- Role-aware authorization guards.
- Celery worker for background email delivery.
- Alembic migrations for schema versioning.

## Tech Stack

- Python 3.11
- FastAPI
- SQLModel + SQLAlchemy (async)
- PostgreSQL
- Redis
- Celery
- Alembic
- Docker Compose
- Pytest

## Project Structure

```
src/
  auth/         # authentication, JWT, account workflows
  books/        # book endpoints and business logic
  reviews/      # review endpoints and logic
  tags/         # tag endpoints and logic
  db/           # database engine, models, redis integration
  celery_tasks.py
  config.py
  middleware.py
migrations/     # alembic migration environment and versions
tests/          # API and auth test coverage
```

## API Docs

Once the app is running locally:

- Swagger UI: http://localhost:8000/api/v1/docs
- OpenAPI JSON: http://localhost:8000/api/v1/openapi.json

## Running Locally With Docker

### 1. Prerequisites

- Docker Desktop installed and running
- Docker Compose v2 (available as `docker compose`)

### 2. Configure Environment Variables

Create a `.env` file in the project root with values for:

- `DATABASE_URL`
- `POSTGRES_USER`
- `POSTGRES_PASSWORD`
- `POSTGRES_DB`
- `REDIS_URL`
- `JWT_SECRET`
- `JWT_ALGORITHM`
- `MAIL_USERNAME`
- `MAIL_PASSWORD`
- `MAIL_SERVER`
- `MAIL_PORT`
- `MAIL_FROM`
- `MAIL_FROM_NAME`
- `DOMAIN`

### 3. Start Services

```bash
docker compose up --build -d
```

### 4. Run Database Migrations

```bash
docker compose exec web alembic upgrade head
```

### 5. Verify Services

```bash
docker compose ps
```

The API should now be reachable on http://localhost:8000.

## Run Tests

```bash
pytest
```

## Highlights

- End-to-end backend ownership: API, data model, auth, async workflows, and background jobs.
- Clean separation of concerns across routes, schemas, and service layers.
- Docker-first developer setup for reproducible local environments.
- Uses migrations and testing as part of regular development workflow.
