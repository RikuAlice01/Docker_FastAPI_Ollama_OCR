---
# 🖼️ OCR FastAPI + Ollama API
---

> 🚀 OCR Web API ที่ใช้ FastAPI และ Ollama รองรับการอัปโหลดภาพเพื่อแปลงเป็นข้อความด้วยโมเดล AI เช่น `llama3.2-vision`.

---

## ✨ Features

- อัปโหลดภาพเพื่อทำ OCR ด้วย AI model (เช่น llama3.2-vision)
- รองรับคำสั่งเสริม (Custom Prompt)
- พัฒนาเร็วด้วย FastAPI
- รองรับ Docker (ใช้งานง่ายบนทุกเครื่อง)
- มี Swagger UI (`/docs`) สำหรับเทสต์ API ได้เลย
- รองรับโมเดล OCR อื่น ๆ ผ่าน Ollama

---

## 📦 Installation

### 1. Clone Repo

```bash
git clone https://github.com/your-username/ocr-fastapi-ollama.git
cd ocr-fastapi-ollama
```

### 2. Build และ Run ด้วย Docker Compose

```bash
docker-compose up --build
```

Docker จะ:

- ติดตั้ง Ollama
- Start Ollama Server
- Pull โมเดล `llama3.2-vision` (ถ้าไม่มีในเครื่อง)
- รัน FastAPI ที่ `http://localhost:8000`

---

## ⚡ Usage

### 🔥 เปิด API Docs (Swagger UI)

เข้า Browser:

```bash
http://localhost:8000/docs
```

Swagger จะให้เรากดเทสต์ API ได้เลย

---

### 📥 POST `/ocr`

- **Description**: อัปโหลดรูปภาพเพื่อทำ OCR
- **Request**: `multipart/form-data`
  - `file`: (Required) ไฟล์ภาพ
  - `prompt`: (Optional) คำสั่งเสริม เช่น "อ่านข้อความในภาพ"

- **Response**:

```json
{
  "ocr_text": "ข้อความที่อ่านได้จากรูปภาพ..."
}
```

### 🛠 ตัวอย่าง `curl`

```bash
curl -X POST "http://localhost:8000/ocr" \
  -F "file=@/path/to/your/image.png" \
  -F "prompt=What is written in this image?"
```

---

## 📖 API Documentation

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST   | `/ocr`    | Upload image for OCR |

---

## 🐛 Troubleshooting

| ปัญหา | วิธีแก้ไข |
|:-------|:----------|
| **Ollama server ไม่ตอบสนอง** | เช็กว่า container `ollama` ทำงานอยู่ หรือรอให้ pull model เสร็จก่อน |
| **โมเดลไม่เจอ / โหลดนาน** | Ollama จะดาวน์โหลด model ครั้งแรก อาจใช้เวลา |
| **Cannot connect to host localhost:11434** | ตรวจสอบว่า `ollama serve` รันอยู่ในเบื้องหลังแล้วใน container |
| **Permission Denied ตอน mount uploads/** | ให้เช็กว่า volume หรือสิทธิ์โฟลเดอร์ให้ Docker เขียนได้ |

---

## 🤝 Contributing

Pull Requests ยินดีต้อนรับ! 🎉  
หากมีข้อเสนอแนะ เช่น:

- รองรับ OCR ภาษาไทย
- เพิ่มตัวเลือก multiple models
- ทำ Web UI สำหรับอัปโหลดไฟล์

ส่ง PR หรือเปิด Issue ได้เลย!

---

## 📜 License

Distributed under the **MIT License**.  
ดูไฟล์ [LICENSE](LICENSE) สำหรับรายละเอียดเพิ่มเติม.

---

## 🛠 Maintainer

**Sitthichai S.**  
Frontend Developer | FastAPI Enthusiast | Docker Lover
