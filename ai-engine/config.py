"""
AutoScale AI Engine configuration.
Central place for engine settings.
"""

APP_NAME = "AutoScale AI Engine"
APP_VERSION = "0.2.0"

# API settings
API_HOST = "0.0.0.0"
API_PORT = 8000

# Project paths
UPLOAD_DIR = "uploads"
TEMP_DIR = "temp"

# AI settings
DEFAULT_CONFIDENCE = 0.5

# CORS settings
ALLOWED_ORIGINS = [
    "https://autoscale-mvp.vercel.app",
    "https://autoscale-mvp.onrender.com",
    "http://localhost:3000",
    "http://localhost:5500"
]
