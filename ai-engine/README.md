# AutoScale AI Engine v0.4.0

Backend API for the AutoScale vehicle comparison project.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## API

- `/` — engine status
- `/health` — health check
- `/cars` — all vehicles
- `/cars/{id}` — vehicle by ID
- `/makes` — available makes
- `/models?make=Honda` — models by make
- `/generations?make=Honda&model=Vezel` — generations
- `/years?make=Honda&model=Vezel&generation=RU` — available years
- `/search?q=Vezel` — text search
- `/compare?car1_id=1&car2_id=2` — vehicle comparison

Vehicle data is stored in `data/cars.json`.
