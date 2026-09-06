from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.database import (
    get_all_cars,
    get_car_by_id,
    get_makes,
    get_models,
    get_generations,
    get_years,
    search_cars
)

app = FastAPI(
    title="AutoScale AI Engine",
    description="Vehicle data and comparison engine for AutoScale",
    version="0.4.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    cars = get_all_cars()
    return {
        "project": "AutoScale AI Engine",
        "version": "0.4.0",
        "status": "online",
        "message": "AutoScale AI Engine is running",
        "cars_loaded": len(cars),
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "engine": "running",
        "version": "0.4.0"
    }


@app.get("/cars")
def cars():
    data = get_all_cars()
    return {
        "count": len(data),
        "cars": data
    }


@app.get("/cars/{car_id}")
def car_by_id(car_id: int):
    car = get_car_by_id(car_id)

    if not car:
        raise HTTPException(status_code=404, detail="Car not found")

    return car


@app.get("/makes")
def makes():
    data = get_makes()
    return {
        "count": len(data),
        "makes": data
    }


@app.get("/models")
def models(make: Optional[str] = None):
    data = get_models(make)
    return {
        "make": make,
        "count": len(data),
        "models": data
    }


@app.get("/generations")
def generations(
    make: Optional[str] = None,
    model: Optional[str] = None
):
    data = get_generations(make, model)
    return {
        "make": make,
        "model": model,
        "count": len(data),
        "generations": data
    }


@app.get("/years")
def years(
    make: Optional[str] = None,
    model: Optional[str] = None,
    generation: Optional[str] = None
):
    data = get_years(make, model, generation)
    return {
        "make": make,
        "model": model,
        "generation": generation,
        "years": data
    }


@app.get("/search")
def search(
    q: Optional[str] = None,
    make: Optional[str] = None,
    model: Optional[str] = None,
    generation: Optional[str] = None,
    year: Optional[int] = None,
    market: Optional[str] = None
):
    data = search_cars(
        q=q,
        make=make,
        model=model,
        generation=generation,
        year=year,
        market=market
    )

    return {
        "count": len(data),
        "filters": {
            "q": q,
            "make": make,
            "model": model,
            "generation": generation,
            "year": year,
            "market": market
        },
        "cars": data
    }


@app.get("/compare")
def compare(car1_id: int, car2_id: int):
    car1 = get_car_by_id(car1_id)
    car2 = get_car_by_id(car2_id)

    if not car1 or not car2:
        raise HTTPException(
            status_code=404,
            detail="One or both cars not found"
        )

    return {
        "car_1": car1,
        "car_2": car2,
        "difference": {
            "length": car1["length"] - car2["length"],
            "width": car1["width"] - car2["width"],
            "height": car1["height"] - car2["height"],
            "wheelbase": car1["wheelbase"] - car2["wheelbase"]
        }
    }
