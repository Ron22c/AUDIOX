import boto3
from botocore.client import Config
from .config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, BUCKET_NAME
from io import BytesIO

# Connect to MinIO (S3-compatible)
s3 = boto3.client(
    's3',
    endpoint_url=MINIO_ENDPOINT,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name='us-east-1'
)

# Ensure bucket exists
def ensure_bucket():
    buckets = s3.list_buckets()
    if BUCKET_NAME not in [b["Name"] for b in buckets.get("Buckets", [])]:
        s3.create_bucket(Bucket=BUCKET_NAME)

# Upload PDF file to bucket
def upload_pdf(file_obj, filename: str):
    ensure_bucket()
    s3.upload_fileobj(
        Fileobj=file_obj,
        Bucket=BUCKET_NAME,
        Key=filename,
        ExtraArgs={"ContentType": "application/pdf"}
    )
    # Generate secure URL (valid for 1 hour)
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': BUCKET_NAME, 'Key': filename},
        ExpiresIn=3600
    )
    return presigned_url