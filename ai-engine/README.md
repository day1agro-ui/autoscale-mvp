# AutoScale AI Engine v1.0

## Files
- main.py — FastAPI API
- config.py — engine configuration
- database.py — vehicle database
- requirements.txt — dependencies

## Local launch
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000

## API
/health
/cars
/brands
/models
/cars/{car_id}
/compare?car1_id=...&car2_id=...
