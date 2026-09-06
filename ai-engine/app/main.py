from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.database import (
    load_cars,
    get_car_by_id,
    search_cars,
    get_makes,
    get_models,
)

app = FastAPI(
    title="AutoScale AI Engine",
    description="Vehicle data, search and comparison engine for AutoScale",
    version="0.3.0",
)

# Allows the GitHub Pages frontend and local development to access the API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "project": "AutoScale AI Engine",
        "version": "0.3.0",
        "status": "online",
        "message": "AutoScale AI Engine is running",
        "docs": "/docs",
        "endpoints": {
            "health": "/health",
            "cars": "/cars",
            "car_by_id": "/cars/{car_id}",
            "search": "/search?q=vezel",
            "compare": "/compare?car1_id=1&car2_id=2",
            "makes": "/makes",
            "models": "/models",
        },
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "engine": "running",
        "version": "0.3.0",
        "vehicles_loaded": len(load_cars()),
    }


@app.get("/cars")
def get_cars():
    cars = load_cars()
    return {
        "count": len(cars),
        "cars": cars,
    }


@app.get("/cars/{car_id}")
def get_car(car_id: int):
    car = get_car_by_id(car_id)

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found",
        )

    return car


@app.get("/search")
def search(
    q: Optional[str] = Query(None, description="Free text search"),
    make: Optional[str] = Query(None),
    model: Optional[str] = Query(None),
    year: Optional[int] = Query(None),
    generation: Optional[str] = Query(None),
    market: Optional[str] = Query(None),
):
    cars = search_cars(
        q=q,
        make=make,
        model=model,
        year=year,
        generation=generation,
        market=market,
    )

    return {
        "count": len(cars),
        "filters": {
            "q": q,
            "make": make,
            "model": model,
            "year": year,
            "generation": generation,
            "market": market,
        },
        "cars": cars,
    }


@app.get("/makes")
def makes():
    data = get_makes()
    return {
        "count": len(data),
        "makes": data,
    }


@app.get("/models")
def models(make: Optional[str] = None):
    data = get_models(make=make)
    return {
        "count": len(data),
        "make": make,
        "models": data,
    }


@app.get("/compare")
def compare_cars(car1_id: int, car2_id: int):
    car1 = get_car_by_id(car1_id)
    car2 = get_car_by_id(car2_id)

    if not car1 or not car2:
        raise HTTPException(
            status_code=404,
            detail="One or both cars not found",
        )

    differences = {
        "length": car1["length"] - car2["length"],
        "width": car1["width"] - car2["width"],
        "height": car1["height"] - car2["height"],
        "wheelbase": car1["wheelbase"] - car2["wheelbase"],
    }

    absolute_difference = {
        key: abs(value)
        for key, value in differences.items()
    }

    return {
        "car_1": car1,
        "car_2": car2,
        "difference": differences,
        "absolute_difference": absolute_difference,
    }
