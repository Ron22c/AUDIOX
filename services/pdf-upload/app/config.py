import os

# MINIO config
MINIO_ENDPOINT = os.getenv("STORAGE_URL", "http://minio:9000")
MINIO_ACCESS_KEY = os.getenv("MINIO_ROOT_USER", "minioadmin")
MINIO_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD", "minioadmin")
BUCKET_NAME = os.getenv("PDF_BUCKET", "pdfs")

# Redis config
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
PDF_UPLOAD_CHANNEL = "pdf_uploaded"