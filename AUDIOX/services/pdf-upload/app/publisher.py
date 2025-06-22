import redis
import json
from .config import REDIS_HOST, REDIS_PORT, PDF_UPLOAD_CHANNEL

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def publish_pdf_uploaded_message(file_url: str, filename: str, timestamp: str):
    message = {
        "filename": filename,
        "url": file_url,
        "uploaded_at": timestamp
    }
    redis_client.publish(PDF_UPLOAD_CHANNEL, json.dumps(message))
