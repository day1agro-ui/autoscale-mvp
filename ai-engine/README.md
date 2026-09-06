# AutoScale AI Engine v0.3.0

Vehicle data, search and comparison backend for AutoScale.

## New architecture

```text
ai-engine/
├── app/
│   ├── __init__.py
│   ├── database.py
│   └── main.py
├── data/
│   └── cars.json
├── config.py
├── requirements.txt
└── README.md
```

## API

- `/` — engine information
- `/health` — health check
- `/cars` — all vehicles
- `/cars/{car_id}` — vehicle by ID
- `/search?q=vezel` — text search
- `/search?make=Honda&year=2015` — structured search
- `/makes` — all makes
- `/models?make=Honda` — models by make
- `/compare?car1_id=1&car2_id=2` — compare two vehicles

## Local start

```bash
uvicorn app.main:app --reload
```

## Render start command

```text
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```
