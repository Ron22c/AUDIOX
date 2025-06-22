from minio import Minio
from .config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, MINIO_BUCKET

client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False,
)

def list_audio_files():
    return [obj.object_name for obj in client.list_objects(MINIO_BUCKET)]

def get_audio_stream(filename: str):
    return client.get_object(MINIO_BUCKET, filename)
