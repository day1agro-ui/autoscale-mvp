"""
AutoScale AI Engine
Main FastAPI application.
"""

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware

from app.vision import analyze_image


app = FastAPI(
    title="AutoScale AI Engine",
    description="AI system for vehicle geometry analysis and realistic visualization.",
    version="0.1.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "project": "AutoScale AI Engine",
        "version": "0.1.0",
        "status": "foundation",
        "message": "AI Engine is running",
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "engine": "AutoScale AI Engine",
    }


@app.post("/analyze-image")
async def analyze_vehicle_image(
    file: UploadFile = File(...)
):
    """
    Upload and perform the first-stage analysis of a vehicle image.
    """

    return await analyze_image(file)
