# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 02-12-2025


from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib

from api.schemas import PredictionRequest, BatchPredictionRequest, PredictionResponse
from api.model_loader import load_model
from api.predict import predict

app = FastAPI(
    title="Immo Price Prediction API",
    description="FastAPI service for predicting real estate prices",
    version="1.0.0"
)

model = "default"

@app.get("/")
def root():
    return {"status": "running", "message": "Welcome to the Immo Price Prediction API!"}

@app.post("/predict", response_model=PredictionResponse)
def predict_single(request: PredictionRequest, model: str = model):
    try:
        pipeline = load_model(model)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"Prediction failed: {str(e)}")

    df = pd.DataFrame([request.model_dump()])
    preds = predict(df, pipeline=pipeline)

    return PredictionResponse(predictions=preds.tolist())

@app.post("/predict/batch", response_model=PredictionResponse)
def predict_batch(request: BatchPredictionRequest, model: str = model):
    try:
        pipeline = load_model(model)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"Prediction failed: {str(e)}")

    df = pd.DataFrame([item.model_dump() for item in request.items])
    preds = predict(df, pipeline=pipeline)

    return PredictionResponse(predictions=preds.tolist())

