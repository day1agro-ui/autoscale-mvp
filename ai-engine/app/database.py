import json
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent
DATABASE_FILE = BASE_DIR / "data" / "cars.json"


def load_cars():
    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_cars():
    return load_cars()


def get_car_by_id(car_id: int):
    return next((car for car in load_cars() if car["id"] == car_id), None)


def get_makes():
    return sorted(set(car["make"] for car in load_cars()))


def get_models(make: Optional[str] = None):
    cars = load_cars()
    if make:
        cars = [car for car in cars if car["make"].lower() == make.lower()]
    return sorted(set(car["model"] for car in cars))


def get_generations(make: Optional[str] = None, model: Optional[str] = None):
    cars = load_cars()

    if make:
        cars = [car for car in cars if car["make"].lower() == make.lower()]

    if model:
        cars = [car for car in cars if car["model"].lower() == model.lower()]

    return sorted(set(car["generation"] for car in cars))


def get_years(
    make: Optional[str] = None,
    model: Optional[str] = None,
    generation: Optional[str] = None
):
    cars = load_cars()

    if make:
        cars = [car for car in cars if car["make"].lower() == make.lower()]

    if model:
        cars = [car for car in cars if car["model"].lower() == model.lower()]

    if generation:
        cars = [
            car for car in cars
            if car["generation"].lower() == generation.lower()
        ]

    years = set()

    for car in cars:
        for year in range(car["year_from"], car["year_to"] + 1):
            years.add(year)

    return sorted(years)


def search_cars(
    q: Optional[str] = None,
    make: Optional[str] = None,
    model: Optional[str] = None,
    generation: Optional[str] = None,
    year: Optional[int] = None,
    market: Optional[str] = None
):
    cars = load_cars()

    if q:
        query = q.lower().strip()
        cars = [
            car for car in cars
            if query in " ".join([
                car["make"],
                car["model"],
                car["generation"],
                car["chassis_code"],
                car["market"],
                car["trim"]
            ]).lower()
        ]

    if make:
        cars = [car for car in cars if car["make"].lower() == make.lower()]

    if model:
        cars = [car for car in cars if car["model"].lower() == model.lower()]

    if generation:
        cars = [
            car for car in cars
            if car["generation"].lower() == generation.lower()
        ]

    if year:
        cars = [
            car for car in cars
            if car["year_from"] <= year <= car["year_to"]
        ]

    if market:
        cars = [
            car for car in cars
            if car["market"].lower() == market.lower()
        ]

    return cars
