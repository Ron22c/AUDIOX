from minio import Minio
from minio.error import S3Error
from config import (
    MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET
)

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)

def upload_to_minio(file_path: str, object_name: str):
    # Ensure bucket exists
    found = client.bucket_exists(MINIO_BUCKET)
    if not found:
        client.make_bucket(MINIO_BUCKET)

    client.fput_object(
        MINIO_BUCKET,
        object_name,
        file_path,
        content_type="audio/mpeg"
    )
    print(f"[MinIO] Uploaded: {object_name}")
