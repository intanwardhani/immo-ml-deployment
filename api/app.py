# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


from fastapi import FastAPI, HTTPException
import pandas as pd
import os

from api.config import MODEL_DIR, DEFAULT_MODEL
from api.schemas import PredictionRequest, BatchPredictionRequest, PredictionResponse
from api.model_loader import load_model
from api.predict import predict

app = FastAPI(
    title="Immo Price Prediction API",
    description="FastAPI service for predicting real estate prices",
    version="1.0.0"
)

DEFAULT_MODEL_NAME = "default"


# -------------------------------
# Health check
# -------------------------------
@app.get("/")
def root():
    return {"status": "running", "message": "Welcome to the Immo Price Prediction API!"}

# -------------------------------
# Version endpoint
# -------------------------------
@app.get("/model/version")
def model_version():
    """
    Returns the version name of the current default model.
    """

    # DEFAULT_MODEL is a symlink → follow it
    model_path = os.path.realpath(DEFAULT_MODEL)

    version_name = os.path.basename(model_path)

    return {
        "default_model": version_name,
        "path": model_path,
    }

# -------------------------------
# Prediction endpoint
# -------------------------------

# Single prediction
@app.post("/predict/{model_name}", response_model=PredictionResponse)
def predict_single(request: PredictionRequest, model_name: str = DEFAULT_MODEL_NAME):
    try:
        pipeline = load_model(model_name)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"Prediction failed: {str(e)}")

    df = pd.DataFrame([request.model_dump()])
    preds = predict(df, pipeline=pipeline)

    return PredictionResponse(predictions=preds.tolist())

# Batch prediction
@app.post("/predict/batch/{model_name}", response_model=PredictionResponse)
def predict_batch(request: BatchPredictionRequest, model_name: str = DEFAULT_MODEL_NAME):
    try:
        pipeline = load_model(model_name)
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=f"Prediction failed: {str(e)}")

    df = pd.DataFrame([item.model_dump() for item in request.items])
    preds = predict(df, pipeline=pipeline)

    return PredictionResponse(predictions=preds.tolist())

