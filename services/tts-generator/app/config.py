import os

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
TAGGED_INPUT_CHANNEL = "tagged_text"

AUDIO_OUTPUT_DIR = "/tmp/audio"
BUCKET_NAME = "audiobooks"
