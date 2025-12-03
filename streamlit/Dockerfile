# ------------------------------
# STREAMLIT DOCKERFILE
# ------------------------------
FROM python:3.11-slim

WORKDIR /app

# Copy requirements
COPY ../requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy ONLY Streamlit code
COPY . /app/streamlit

EXPOSE 8501

CMD ["streamlit", "run", "streamlit/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
