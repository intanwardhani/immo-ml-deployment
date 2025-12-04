# ===============================
# Streamlit Frontend Dockerfile
# ===============================

FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY ../requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy Streamlit folder
COPY . /app/streamlit

ENV PYTHONPATH=/app

EXPOSE 8501

# Start Streamlit
CMD ["streamlit", "run", "streamlit/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
