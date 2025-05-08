#!/bin/bash

# Start FastAPI backend
echo "Starting FastAPI backend..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Wait to ensure backend starts
sleep 5

# Start Streamlit frontend
echo "Starting Streamlit frontend..."
streamlit run streamlit_app.py --server.port 8501
