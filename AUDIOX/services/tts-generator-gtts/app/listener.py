import redis
import json
from tts import synthesize, combine_audio_segments
from minio_utils import upload_to_minio
from config import REDIS_HOST, REDIS_PORT, TAGGED_INPUT_CHANNEL

def handle_message(message):
    data = json.loads(message['data'])
    filename = data["filename"]
    segments = data["tagged_segments"]

    for i, seg in enumerate(segments):
        text = seg["text"]
        audio_name = f"{filename}-seg{i}"
        synthesize(text, audio_name)

    final_path = combine_audio_segments(filename, len(segments))

    # Upload to MinIO
    upload_to_minio(final_path, f"{filename}_final.mp3")
