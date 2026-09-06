from fastapi import FastAPI, UploadFile, File, HTTPException
from PIL import Image
from io import BytesIO

app = FastAPI(
    title="AutoScale AI Engine",
    description="AI system for vehicle geometry analysis and realistic visualization.",
    version="0.1.0",
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
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="Uploaded file must be an image.",
        )

    content = await file.read()

    try:
        image = Image.open(BytesIO(content))
        width, height = image.size
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail="Unable to read image.",
        ) from exc

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "image_width": width,
        "image_height": height,
        "status": "received",
        "next_stage": "vehicle detection",
    }
