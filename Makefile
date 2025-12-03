# ================================
# These targets are not files
# Always run the commands when invoked
# ================================

.PHONY: api streamlit dev docker-build up upd down down-v logs test-api format clean

# ================================
# Makefile for FastAPI + Streamlit
# Hybrid: Local dev + Docker deploy
# ================================

# ---- VARIABLES ----
API_HOST=127.0.0.1
API_PORT=8000
STREAMLIT_PORT=8501

# ================================
# LOCAL DEVELOPMENT COMMANDS
# ================================

# Run FastAPI locally (no Docker)
api:
	uvicorn api.app:app --reload --host $(API_HOST) --port $(API_PORT)

# Run Streamlit locally (no Docker)
streamlit:
	streamlit run streamlit/app.py --server.port $(STREAMLIT_PORT)

# Run both FastAPI & Streamlit locally in two terminals
dev:
	@echo "Open two terminals and run:"
	@echo "  make api"
	@echo "  make streamlit"

# ================================
# DOCKER COMMANDS
# ================================

# Build Docker images
docker-build:
	docker compose build

# Start both API + Streamlit with Docker
up:
	docker compose up --build

# Run in detached mode
upd:
	docker compose up --build -d

# Stop running containers
down:
	docker compose down

# Remove containers + volumes if needed
down-v:
	docker compose down -v

# Show logs
logs:
	docker compose logs -f

# ================================
# UTILITIES
# ================================

# Test API server locally
test-api:
	curl http://$(API_HOST):$(API_PORT)/docs

# Linting (optional if you use Black)
format:
	black .

# Clean Python cache files
clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
