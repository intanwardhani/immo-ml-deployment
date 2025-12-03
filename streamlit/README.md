# Streamlit Frontend for Immo Price Predictor
This directory contains the UI code for the price prediction app.

# Files
- `app.py`      : Main Streamlit UI
- `client.py`   : Handles communication with FastAPI backend
- `config.py`
- Dockerfile
- `utils.py`    : Helper functions (Yes/No conversion)

# Running Streamlit
1. Start the API
```
uvicorn api.app:app --reload
```

2. Start the Streamlit UI
```
streamlit run streamlit/app.py
```

3. Frontend will open at
```
[http://localhost:8501](http://localhost:8501)
```
