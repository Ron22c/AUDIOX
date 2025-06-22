# 📖 PDF to Bengali Audio Story App – Architecture & Design Summary

## 🧩 System Overview

This system converts uploaded Bengali PDF books into emotion-aware audio stories and streams them to a React Native iOS app.

---

## 🏗️ Architecture Diagram (Textual)

```text
USER
│
├─▶ 📄 PDF Upload Service (FastAPI)
│     ├─ Uploads PDF to MinIO (`pdfs` bucket)
│     └─ Publishes message to Redis (`pdf_uploaded`)
│
├─▶ 🧠 Text Extraction Service
│     ├─ Subscribes to `pdf_uploaded`
│     ├─ Uses Tesseract OCR (Bengali supported)
│     └─ Publishes cleaned text to Redis (`text_extracted`)
│
├─▶ 🧠 Emotion Tagging Service
│     ├─ Subscribes to `text_extracted`
│     ├─ Splits text into segments
│     └─ Tags segments with basic emotions
│        Publishes to Redis (`tagged_text`)
│
├─▶ 🔊 TTS Generator (gTTS + pydub)
│     ├─ Subscribes to `tagged_text`
│     ├─ Generates MP3s per segment (Bengali)
│     ├─ Combines all into one story MP3
│     └─ Uploads final MP3 to MinIO (`audio` bucket)
│
├─▶ 🌐 Audio API (FastAPI)
│     ├─ Lists available stories from MinIO
│     └─ Streams audio files to clients
│
└─▶ 📱 React Native Mobile App (iOS)
      ├─ Fetches story list from Audio API
      └─ Streams MP3 using `react-native-track-player`
```

## 🧪 Components & Technologies

| Component             | Tech Stack / Tool                                |
|-----------------------|--------------------------------------------------|
| **PDF Upload**        | FastAPI + MinIO                                  |
| **Text Extraction**   | Tesseract OCR (`pytesseract`, Bengali language)  |
| **Emotion Tagging**   | Python NLP + Rule-based tagging                  |
| **TTS Generator**     | gTTS (offline) + pydub for MP3 merge             |
| **Audio Storage**     | MinIO (S3-compatible object storage)             |
| **Queueing**          | Redis Pub/Sub                                    |
| **Audio API**         | FastAPI                                          |
| **Mobile App**        | React Native (iOS) + `react-native-track-player` |

---

## 🔁 Redis Channels Used

| Channel Name      | Payload Sent                        |
|-------------------|-------------------------------------|
| `pdf_uploaded`    | `{ "filename": "book1.pdf" }`       |
| `text_extracted`  | `{ "filename": "book1", "text": "..." }` |
| `tagged_text`     | `{ "filename": "book1", "tagged_segments": [...] }` |

---

## 📂 MinIO Buckets

| Bucket     | Usage                     |
|------------|---------------------------|
| `pdfs`     | Raw uploaded PDF files    |
| `audio`    | Final combined MP3 files  |

---

## 📱 Mobile App Behavior (React Native)

- Lists stories using `GET /stories`
- Plays story via `GET /stories/{id}`
- Uses `react-native-track-player` for smooth playback (iOS compatible)
- Backend must be accessible via IP or tunnel (e.g. ngrok)

---

## 🔒 Optional Next Steps

- ✅ Add cover metadata, description, author, emotion
- ✅ Add background processing support in mobile
- ✅ Support offline downloads with `react-native-fs`
- ✅ Add authentication to API
- ✅ Use signed URLs or JWT to protect audio files

---

## 📦 Docker Compose Services

- `pdf_upload_service`
- `text_extraction_service`
- `emotion_tagger_service`
- `tts_generator_gtts`
- `audio_api`
- `redis`
- `minio`


---

## 🧪 API Test with cURL

Use these cURL requests to test your services from terminal or scripts.

> Replace `localhost:8000` with your actual IP (e.g. `192.168.0.x:8000`) if testing from mobile or other devices.

---

### 🔹 1. List Available Stories

**Endpoint**: `GET /stories`

```bash
curl http://localhost:8000/stories
✅ Expected Response:
{
  "stories": [
    "book1_final.mp3",
    "book2_final.mp3"
  ]
}
🔹 2. Stream a Specific Story
Endpoint: GET /stories/{story_id}

curl http://localhost:8000/stories/book1 --output book1.mp3
✅ Saves the streamed MP3 to a local file called book1.mp3.

To just stream it without saving:

curl http://localhost:8000/stories/book1
Or stream with a player (like VLC):

vlc http://localhost:8000/stories/book1
(Optional) 🔹 3. Upload a PDF (if implemented)
If you have or plan to create a POST /upload endpoint in your PDF Upload service:

curl -X POST http://localhost:8001/upload \
  -F "file=@book1.pdf"

✅ This would trigger the full pipeline (PDF → MP3).

```

# 🐳 Steps to Run Docker with Docker Compose (macOS)

## 📥 1. Download Docker Desktop

Download Docker Desktop for Mac from the official website:

👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

---

## 💾 2. Install Docker

1. Open the downloaded `.dmg` file.
2. Drag the **Docker** icon into the **Applications** folder.

---

## 🚀 3. Launch Docker

- Open **Docker** from your **Applications**.
- You may be prompted to log in with your Docker Hub account.

Wait for Docker to fully start (look for the Docker whale icon in your menu bar).

---

## ⚙️ 4. Build and Run Containers

Navigate to your project directory in the terminal where your `docker-compose.yml` file is located, then run:

```bash
docker-compose up --build
```
