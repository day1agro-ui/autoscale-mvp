"""
AutoScale AI Engine
Computer Vision module.

This module is responsible for the first stage of image processing:
- receiving an image;
- reading image metadata;
- basic validation;
- preparing the foundation for vehicle detection and geometry extraction.
"""

from io import BytesIO
from typing import Dict, Any

from fastapi import UploadFile, HTTPException
from PIL import Image


ALLOWED_IMAGE_TYPES = {
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/webp",
}


async def analyze_image(file: UploadFile) -> Dict[str, Any]:
    """
    Perform basic image analysis.

    At the current v0.1 stage this function validates the uploaded image
    and returns its technical metadata. Vehicle detection will be added
    in the next development stage.
    """

    if not file:
        raise HTTPException(
            status_code=400,
            detail="Image file is required."
        )

    if file.content_type not in ALLOWED_IMAGE_TYPES:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported image format. "
                "Use JPEG, PNG or WEBP."
            )
        )

    try:
        content = await file.read()

        if not content:
            raise HTTPException(
                status_code=400,
                detail="Uploaded image is empty."
            )

        image = Image.open(BytesIO(content))
        image.verify()

        image = Image.open(BytesIO(content))

        width, height = image.size

        return {
            "status": "success",
            "image": {
                "filename": file.filename,
                "format": image.format,
                "width": width,
                "height": height,
                "mode": image.mode,
            },
            "analysis": {
                "vehicle_detected": False,
                "stage": "basic_image_analysis",
                "next_stage": "vehicle_detection",
            },
        }

    except HTTPException:
        raise

    except Exception as error:
        raise HTTPException(
            status_code=400,
            detail=f"Unable to process image: {str(error)}"
        )
