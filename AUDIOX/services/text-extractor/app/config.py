import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
PDF_UPLOAD_CHANNEL = "pdf_uploaded"

TEMP_DIR = "/tmp/pdfs"
