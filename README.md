# FastAPI Product Management API

A REST API for managing products, built with FastAPI and PostgreSQL.

## Tech Stack

- **FastAPI** 0.135.1 — web framework with automatic Swagger docs
- **SQLAlchemy** — ORM for database interaction
- **PostgreSQL** — database
- **Pydantic** 2.12.5 — request/response validation
- **Uvicorn** 0.41.0 — ASGI server

## Project Structure

```
FAST_API/
├── main.py              # API endpoints
├── models.py            # Pydantic schemas
├── database_models.py   # SQLAlchemy ORM models
├── config.py            # Database configuration
└── requirements.txt     # Dependencies
```

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL running on `localhost:5432`

### Installation

```bash
# Create and activate virtual environment
python -m venv myenv
source myenv/bin/activate  # Windows: myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Database Configuration

Update the connection string in `config.py`:

```python
DATABASE_URL = "postgresql://<user>:<password>@localhost:5432/<dbname>"
```

### Run the Server

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/products` | Get all products |
| GET | `/product/{id}` | Get product by ID |
| POST | `/products` | Create a new product |
| PUT | `/product/{id}` | Update a product |
| DELETE | `/product?id={id}` | Delete a product |

## Product Schema

```json
{
  "id": 1,
  "name": "Phone",
  "description": "A smartphone",
  "price": 699.99,
  "quantity": 50
}
```

## Interactive Docs

Once the server is running:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Notes

- CORS is configured for a frontend running on `http://localhost:3000`
- The database is seeded with sample products on first run
