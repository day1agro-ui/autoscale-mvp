"""
AutoScale vehicle database layer.
Loads vehicle data from data/cars.json.
"""

import json
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "cars.json"


def load_cars() -> list[dict]:
    """Load all vehicles from the JSON database."""
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)

    return data


def get_car_by_id(car_id: int) -> Optional[dict]:
    """Return one vehicle by ID."""
    return next((car for car in load_cars() if car["id"] == car_id), None)


def search_cars(
    q: Optional[str] = None,
    make: Optional[str] = None,
    model: Optional[str] = None,
    year: Optional[int] = None,
    generation: Optional[str] = None,
    market: Optional[str] = None,
) -> list[dict]:
    """
    Search vehicles using text and structured filters.
    All supplied filters are combined.
    """
    cars = load_cars()

    if q:
        query = q.lower().strip()

        def matches_query(car: dict) -> bool:
            haystack = " ".join(
                str(car.get(field, ""))
                for field in [
                    "make",
                    "model",
                    "generation",
                    "year",
                    "market",
                    "body_type",
                ]
            ).lower()
            return query in haystack

        cars = [car for car in cars if matches_query(car)]

    if make:
        cars = [car for car in cars if car["make"].lower() == make.lower()]

    if model:
        cars = [car for car in cars if car["model"].lower() == model.lower()]

    if year is not None:
        cars = [car for car in cars if car["year"] == year]

    if generation:
        cars = [
            car for car in cars
            if car["generation"].lower() == generation.lower()
        ]

    if market:
        cars = [
            car for car in cars
            if car.get("market", "").lower() == market.lower()
        ]

    return cars


def get_makes() -> list[str]:
    """Return sorted unique vehicle makes."""
    return sorted({car["make"] for car in load_cars()})


def get_models(make: Optional[str] = None) -> list[str]:
    """Return sorted unique models, optionally filtered by make."""
    cars = load_cars()

    if make:
        cars = [car for car in cars if car["make"].lower() == make.lower()]

    return sorted({car["model"] for car in cars})
