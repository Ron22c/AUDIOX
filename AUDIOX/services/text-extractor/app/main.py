from listener import handle_message
from config import REDIS_HOST, REDIS_PORT, PDF_UPLOAD_CHANNEL
import redis

def main():
    print(f"[👂] Starting Text Extraction Service... (listening on {PDF_UPLOAD_CHANNEL})")
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe(PDF_UPLOAD_CHANNEL)

    for message in pubsub.listen():
        if message['type'] == 'message':
            handle_message(message)

if __name__ == "__main__":
    main()
