# ===============================
# FastAPI API Dockerfile
# ===============================

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy API folder
COPY . /app/api

# Copy models folder one level up
COPY ../models /app/models

ENV PYTHONPATH=/app

# Expose FastAPI port
EXPOSE 8000

# Start API
CMD ["uvicorn", "api.app:app", "--host", "0.0.0.0", "--port", "8000"]
