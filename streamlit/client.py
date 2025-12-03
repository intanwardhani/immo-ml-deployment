# UTF-8 Python 3.13.5
# Author: Intan K. Wardhani
# Last modified: 03-12-2025


import requests

API_URL = "http://127.0.0.1:8000"

def call_api(model_name: str, payload: dict):
    url = f"{API_URL}/predict/{model_name}"
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        
        if response.status_code != 200:
            return {"error": response.text}
        
        return response.json()
    
    except Exception as e:
        return {"error": str(e)}
