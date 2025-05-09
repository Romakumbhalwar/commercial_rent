#!/bin/bash

# Start FastAPI app (backend)
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Wait a bit to ensure FastAPI starts before Streamlit
sleep 5

# Start Streamlit app (frontend)
streamlit run app/streamlit_app.py --server.port 3000

