![](https://img.shields.io/badge/Python-14354C?style=flat&logo=python&logoColor=white) ![](https://img.shields.io/badge/Markdown-000000?style=flat&logo=markdown&logoColor=white) ![](https://img.shields.io/badge/macOS-000000?style=flat&logo=apple&logoColor=white) 

# About Me
Machine learning and deployment were new to me. No doubt, it was daunting and a very intense learning process. However, more than anything, it challenged my patience, conscientiousness, grit, and adaptability in learning something new, complex, and outside of my comfort zone. This project has provided me with not only some hands-on fundamentals of machine-learning and (somewhat) production-ready deployment, but also the structural thinking to tackle future projects. I still have many things to learn and practise (always do), but now I feel equipped to do just that :wink:

# Overview
This is part of the Machine Learning solo project at BeCode Data Science &amp; AI Bootcamp 2025. This deployment repository is auto-synced with my [training repository](https://github.com/intanwardhani/immo-ml-training). This autosync allows model trainings to be done separately in the training repo with each recently-trained model versioned and pushed automatically into this deployment repo.

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
- Create models autosync from training repo to the deployment
- Fix issues with FastAPI
- Fix issues with streamlit
- Check FastAPI + streamlit connection locally



# How To Run
To run both services (the API and streamlit) locally, run the following command in the project root's terminal: `make api` and `make streamlit`. After both services start, visit:
- (FastAPI)
- (streamlit)

To run the deployed services, run the following command in your webbrowser:



# Project Structure
Models were trained in the [related](https://github.com/intanwardhani/immo-ML-project) repository and automatically synchronised by Github Action agent into the `models/` folder.

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
├── ml_components/
│   ├── __init__.py
│   └── transformers.py
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

