# AutoScale AI Engine

AI backend for the AutoScale project.

## v0.1 Foundation

- FastAPI service
- Health endpoint
- Image upload endpoint
- Image metadata extraction
- OpenAPI documentation

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

- `/` — service status
- `/health` — health check
- `/docs` — API documentation
