---
# 🖼️ OCR FastAPI + Ollama API
---

> 🚀 An OCR Web API powered by FastAPI and Ollama, supporting image uploads to extract text using AI models like `llama3.2-vision`.

---

## ✨ Features

- Upload images for OCR processing using AI models (e.g., llama3.2-vision)
- Support for custom prompts
- Rapid development with FastAPI
- Docker support (easy deployment on any machine)
- Built-in Swagger UI (`/docs`) for testing APIs
- Supports other OCR models via Ollama

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ocr-fastapi-ollama.git
cd ocr-fastapi-ollama
```

### 2. Build and Run with Docker Compose

```bash
docker-compose up --build
```

Docker will:

- Install Ollama
- Start the Ollama Server
- Pull the `llama3.2-vision` model (if not already available locally)
- Run FastAPI at `http://localhost:8000`

---

## ⚡ Usage

### 🔥 Open API Docs (Swagger UI)

In your browser, navigate to:

```bash
http://localhost:8000/docs
```

You can interact with and test the API directly from the Swagger UI.

---

### 📥 POST `/ocr`

- **Description**: Upload an image to perform OCR.
- **Request**: `multipart/form-data`
  - `file`: (Required) The image file.
  - `prompt`: (Optional) Custom prompt, e.g., "Read the text in the image."

- **Response**:

```json
{
  "ocr_text": "Extracted text from the image..."
}
```

### 🛠 Example `curl` Command

```bash
curl -X POST "http://localhost:8000/ocr" \
  -F "file=@/path/to/your/image.png" \
  -F "prompt=What is written in this image?"
```

---

## 📖 API Documentation

| Method | Endpoint | Description         |
|--------|----------|---------------------|
| POST   | `/ocr`    | Upload image for OCR |

---

## 🐛 Troubleshooting

| Problem | Solution |
|:--------|:---------|
| **Ollama server not responding** | Make sure the `ollama` container is running, or wait until the model is fully pulled. |
| **Model not found / slow loading** | Ollama downloads the model the first time, which may take a while. |
| **Cannot connect to host localhost:11434** | Ensure `ollama serve` is running in the background inside the container. |
| **Permission denied when mounting uploads/** | Check that the volume or folder permissions allow Docker to write. |

---

## 🤝 Contributing

Pull Requests are welcome! 🎉  
Suggestions such as:

- Thai language OCR support
- Multiple model selection
- Web UI for uploading files

Feel free to open a PR or an Issue!

---

## 📜 License

Distributed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🛠 Maintainer

**Sitthichai S.**  
Frontend Developer | FastAPI Enthusiast | Docker Lover

---
