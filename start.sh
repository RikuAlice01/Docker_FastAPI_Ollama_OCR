#!/bin/bash

# รอให้ ollama พร้อม
echo "Waiting for Ollama to be ready..."
sleep 10

# Pull โมเดล llama3.2-vision
echo "Pulling llama3.2-vision model..."
curl -X POST http://ollama:11434/api/pull -d '{"name": "llama3.2-vision"}'

# เริ่ม FastAPI
echo "Starting FastAPI..."
exec uvicorn main:app --host 0.0.0.0 --port 8000 --reload
