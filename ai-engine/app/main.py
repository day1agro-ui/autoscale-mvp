from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="AutoScale AI Engine",
    description="Vehicle data and comparison engine for AutoScale",
    version="0.3.0"
)


# --------------------------------------------------
# CORS
# Allows the Vercel frontend to communicate with API
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://autoscale-mvp.vercel.app",
        "https://autoscale-mvp-git-main-day1agro-ui.vercel.app",
        "http://localhost:3000",
        "http://127.0.0.1:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------------------------------------
# TEMPORARY MVP VEHICLE DATABASE
# All dimensions are in millimeters
# --------------------------------------------------

cars = [
    {
        "id": 1,
        "make": "Honda",
        "model": "Vezel",
        "generation": "RU1",
        "year": 2015,
        "length": 4295,
        "width": 1770,
        "height": 1605,
        "wheelbase": 2610
    },
    {
        "id": 2,
        "make": "Volkswagen",
        "model": "T-Cross",
        "generation": "1st Generation",
        "year": 2021,
        "length": 4110,
        "width": 1760,
        "height": 1584,
        "wheelbase": 2551
    },
    {
        "id": 3,
        "make": "Volkswagen",
        "model": "T-Roc",
        "generation": "1st Generation",
        "year": 2020,
        "length": 4234,
        "width": 1819,
        "height": 1573,
        "wheelbase": 2603
    },
    {
        "id": 4,
        "make": "Subaru",
        "model": "Levorg",
        "generation": "VM",
        "year": 2016,
        "length": 4690,
        "width": 1780,
        "height": 1490,
        "wheelbase": 2650
    }
]


@app.get("/")
def root():
    return {
        "project": "AutoScale AI Engine",
        "version": "0.3.0",
        "status": "online",
        "message": "AutoScale AI Engine is running",
        "docs": "/docs"
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "engine": "running",
        "version": "0.3.0"
    }


@app.get("/cars")
def get_cars():
    return {
        "count": len(cars),
        "cars": cars
    }


@app.get("/cars/{car_id}")
def get_car(car_id: int):

    car = next(
        (item for item in cars if item["id"] == car_id),
        None
    )

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    return car


@app.get("/compare")
def compare_cars(car1_id: int, car2_id: int):

    car1 = next(
        (item for item in cars if item["id"] == car1_id),
        None
    )

    car2 = next(
        (item for item in cars if item["id"] == car2_id),
        None
    )

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


@app.get("/api/info")
def api_info():

    return {
        "engine": "AutoScale AI Engine",
        "version": "0.3.0",
        "vehicles_loaded": len(cars),
        "status": "online"
    }
