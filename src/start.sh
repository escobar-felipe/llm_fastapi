#!/bin/sh

# Check if APP_ENV is "prod", "local", or "dev" and run Uvicorn accordingly
if [ "$APP_ENV" = "prod" ]; then
    uvicorn --host 0.0.0.0 --port 80 --workers 2 main:app
elif [ "$APP_ENV" = "local" ]; then
    python -m debugpy --listen 0.0.0.0:5678 -m uvicorn --host 0.0.0.0 --port 8081 --workers 2 --reload main:app
else
    uvicorn --host 0.0.0.0 --port 8081 --workers 2 --reload main:app
fi
