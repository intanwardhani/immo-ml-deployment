# About Me

# Overview
This is part of the Machine Learning solo project at BeCode Data Science &amp; AI Bootcamp 2025.

# Timeline
--- Day 1 (1 Dec 2025) ---
- Introduction to the project
- Learn FastApi, Docker, and Streamlit
- Design project structure

--- Day 2 (2 Dec 2025) ---
- Deeper understanding of FastApi, Docker, and Streamlit
- Build prototype project's API
- Build prototype streamlit webapp
- Start UI design

--- Day 3 (3 Dec 2025) ---
- Complete UI design
- Adjust FastAPI and streamlit services
- Create a Makefile (hybrid Docker + non-Docker containerisation)
- Version models and connect the training repo with this repo

--- Day 4 (4 Dec 2025) ---
- 


# How To Run
To run both services (the API and streamlit), run the following command in the project root's terminal: `make api` and `make streamlit`. After both services start, visit:
- http://127.0.0.1:8000 (FastAPI)
- http://127.0.0.1:8501 (streamlit)


# Project Structure
Models were trained in the [https://github.com/intanwardhani/immo-ML-project](related) repository and copied here into the `models/` folder.

```markdown
immo-ml-deployment/
│
├── api/
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── Dockerfile
│   ├── model_loader.py
│   ├── predict.py
│   ├── schemas.py
│   └── README.md
│
├── models/
│   ├── RandomForest_pipeline_latest.pkl
│   ├── Ridge_pipeline_latest.pkl
│   ├── XGBoost_pipeline_latest.pkl
│   └── README.md
│
├── streamlit/
│   ├── app.py
│   ├── client.py
│   ├── config.py
│   ├── Dockerfile
│   ├── utils.py
│   └── README.md
│
├── .gitignore
├── docker-compose.yml
├── Makefile
├── requirements.txt
├── LICENSE
└── README.md
```

