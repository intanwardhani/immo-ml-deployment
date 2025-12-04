# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, "models")

# Default = latest version symlink
DEFAULT_MODEL = os.path.join(MODEL_DIR, "XGBoost_pipeline_latest.pkl")
