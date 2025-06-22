import redis
import json
import os
from .config import REDIS_HOST, REDIS_PORT, TAGGED_INPUT_CHANNEL, AUDIO_OUTPUT_DIR
from .tts import synthesize

def handle_message(message):
    data = json.loads(message['data'])
    filename = data["filename"]
    segments = data["tagged_segments"]

    output_audio_paths = []

    for i, seg in enumerate(segments):
        text = seg["text"]
        emotion = seg["emotion"]
        audio_name = f"{filename}-seg{i}"
        audio_path = synthesize(text, audio_name, emotion)
        output_audio_paths.append(audio_path)

    print(f"[🎧] Synthesized audio for {len(segments)} segments.")
