import redis
from redis import Redis
import json
import os
import requests
from config import REDIS_HOST, REDIS_PORT, PDF_UPLOAD_CHANNEL, TEMP_DIR
from extract import extract_text_from_pdf

redis_client = Redis(host="redis", port=6379, decode_responses=True)

def download_pdf(url: str, dest_path: str):
    response = requests.get(url)
    with open(dest_path, 'wb') as f:
        f.write(response.content)

def handle_message(message):
    data = json.loads(message['data'])
    filename = data["filename"]
    url = data["url"]
    print(f"[🔔] New PDF uploaded: {filename}")

    os.makedirs(TEMP_DIR, exist_ok=True)
    filepath = os.path.join(TEMP_DIR, filename)
    
    # Download the PDF from MinIO
    print(f"[⬇️] Downloading PDF from {url}...")
    download_pdf(url, filepath)
    
    # Extract text
    print(f"[📖] Extracting Bengali text...")
    extracted_text = extract_text_from_pdf(filepath)
    
    # Save or forward (mock for now)
    output_path = os.path.join(TEMP_DIR, f"{filename}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(extracted_text)
    
    print(f"[✅] Extraction complete. Text saved to {output_path}")

    redis_client.publish("text_extracted", json.dumps({
        "filename": filename,
        "text": extracted_text
    }))