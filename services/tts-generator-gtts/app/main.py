from listener import handle_message
from config import REDIS_HOST, REDIS_PORT, TAGGED_INPUT_CHANNEL
import redis

def main():
    print(f"[TTS-GTTS] Listening on Redis channel: {TAGGED_INPUT_CHANNEL}")
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    pubsub = r.pubsub()
    pubsub.subscribe(TAGGED_INPUT_CHANNEL)

    for message in pubsub.listen():
        if message['type'] == 'message':
            handle_message(message)

if __name__ == "__main__":
    main()
