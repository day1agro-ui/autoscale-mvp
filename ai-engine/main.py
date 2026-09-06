from fastapi import FastAPI

app = FastAPI(
    title="AutoScale AI Engine",
    description="AI system for vehicle geometry analysis and realistic visualization",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "project": "AutoScale AI Engine",
        "version": "0.1.0",
        "status": "foundation",
        "message": "AI Engine is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "engine": "AutoScale AI Engine"
    }
