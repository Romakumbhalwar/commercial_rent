#!/bin/bash

# Start FastAPI server (in the background)
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit app
streamlit run streamlit_app.py
