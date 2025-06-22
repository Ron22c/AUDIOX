import redis
import json
from config import REDIS_HOST, REDIS_PORT, TEXT_INPUT_CHANNEL, TAGGED_OUTPUT_CHANNEL
from emotion import structure_and_tag

def handle_message(message):
    data = json.loads(message['data'])
    filename = data.get("filename")
    text = data.get("text")

    print(f"[🧠] Tagging text for: {filename}")

    structured = structure_and_tag(text)

    result = {
        "filename": filename,
        "tagged_segments": structured
    }

    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    r.publish(TAGGED_OUTPUT_CHANNEL, json.dumps(result))
    print(f"[✅] Published emotion-tagged output.")
