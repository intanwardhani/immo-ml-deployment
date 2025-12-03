# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


import os

# BASE_DIR should be project root (one level above api/)
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Default model file name (just the filename, not full path)
DEFAULT_MODEL = "XGBoost_pipeline.pkl"
