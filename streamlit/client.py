# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


import requests
import os

# ================================
# CHANGES:
# 1. Added automatic API URL switching:
#    - local: 127.0.0.1:8000
#    - docker-compose service: http://api:8000
# 2. Model endpoint updated to /predict?model={model_name}
# 3. Added better error handling
# ================================

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

def call_api(model_name: str, payload: dict):
    # Ensure model filename is used (e.g., "XGBoost_pipeline.pkl")
    url = f"{API_URL}/predict?model={model_name}"
    
    try:
        response = requests.post(url, json=payload, timeout=10)

        if response.status_code != 200:
            return {
                "error": f"API Error {response.status_code}",
                "details": response.text
            }
        return response.json()
    
    except Exception as e:
        return {"error": f"Connection failed: {str(e)}"}

    

