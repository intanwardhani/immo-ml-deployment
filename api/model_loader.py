# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


import joblib
import os
from functools import lru_cache
from api.config import DEFAULT_MODEL, MODEL_DIR


@lru_cache(maxsize=5)
def load_model(model_name: str = "default"):
    """
    Load a model pipeline by name.
    """
    if model_name == "default":
        model_name = DEFAULT_MODEL
    path = os.path.join(MODEL_DIR, model_name)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Model not found: {path}")
    return joblib.load(path)

