import os
import shutil
from uuid import uuid4

from fastapi import FastAPI, UploadFile, File, HTTPException
import ollama

# Create uploads folder
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

# Use OLLAMA_HOST from the environment (docker-compose)
ollama_base_url = os.getenv("OLLAMA_HOST", "http://localhost:11434")
ollama_client = ollama.Client(host=ollama_base_url)

# OCR Helper
async def ocr_with_ollama(image_path: str, model: str = "llama3.2-vision", prompt: str = "What is written in this image?") -> str:
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        response = ollama_client.chat(
            model=model,
            messages=[{"role": "user", 
                       "content": prompt,
                       "images": [image_bytes]
                       }],
        )

        return response['message']['content']
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR Error: {e}")

# API: Upload image and OCR
@app.post("/ocr")
async def upload_image(file: UploadFile = File(...), prompt: str = "What is written in this image?"):
    try:
        file_ext = file.filename.split(".")[-1]
        unique_filename = f"{uuid4()}.{file_ext}"
        file_path = os.path.join(UPLOAD_DIR, unique_filename)

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Perform OCR
        ocr_result = await ocr_with_ollama(file_path, prompt=prompt)

        # Cleanup
        os.remove(file_path)

        return {"ocr_text": ocr_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File upload/OCR failed: {e}")
