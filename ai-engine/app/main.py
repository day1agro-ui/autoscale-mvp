from fastapi import FastAPI, HTTPException, Query
from config import APP_NAME, APP_VERSION
from database import cars

app = FastAPI(
    title=APP_NAME,
    description="Vehicle data and comparison engine for AutoScale",
    version=APP_VERSION
)


def find_car(car_id: str):
    return next((car for car in cars if car["id"] == car_id), None)


@app.get("/")
def root():
    return {
        "project": APP_NAME,
        "version": APP_VERSION,
        "status": "online",
        "message": "AutoScale AI Engine is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "engine": "running",
        "version": APP_VERSION,
        "cars_loaded": len(cars)
    }


@app.get("/cars")
def get_cars(
    make: str | None = None,
    model: str | None = None,
    q: str | None = Query(default=None, description="Search query")
):
    result = cars

    if make:
        result = [car for car in result if car["make"].lower() == make.lower()]

    if model:
        result = [car for car in result if car["model"].lower() == model.lower()]

    if q:
        needle = q.lower()
        result = [
            car for car in result
            if needle in " ".join(
                str(car.get(key, ""))
                for key in ["make", "model", "generation", "version", "engine"]
            ).lower()
        ]

    return {"count": len(result), "cars": result}


@app.get("/brands")
def get_brands():
    brands = sorted(set(car["make"] for car in cars))
    return {"count": len(brands), "brands": brands}


@app.get("/models")
def get_models(make: str | None = None):
    result = cars
    if make:
        result = [car for car in result if car["make"].lower() == make.lower()]

    models = sorted(set(car["model"] for car in result))
    return {"count": len(models), "models": models}


@app.get("/cars/{car_id}")
def get_car(car_id: str):
    car = find_car(car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    return car


@app.get("/compare")
def compare_cars(car1_id: str, car2_id: str):
    car1 = find_car(car1_id)
    car2 = find_car(car2_id)

    if not car1 or not car2:
        raise HTTPException(
            status_code=404,
            detail="One or both cars not found"
        )

    dimensions = ["length", "width", "height", "wheelbase"]

    difference = {
        key: car1[key] - car2[key]
        for key in dimensions
    }

    absolute_difference = {
        key: abs(car1[key] - car2[key])
        for key in dimensions
    }

    return {
        "car_1": car1,
        "car_2": car2,
        "difference": difference,
        "absolute_difference": absolute_difference
    }
