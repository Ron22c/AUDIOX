import random

EMOTIONS = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise', 'neutral']

def segment_text(text: str) -> list:
    # Simple sentence splitter
    return [s.strip() for s in text.split("।") if s.strip()]

def tag_emotion(sentence: str) -> str:
    # Placeholder — replace with ML model later
    return random.choice(EMOTIONS)

def structure_and_tag(text: str):
    segments = segment_text(text)
    return [{"text": seg, "emotion": tag_emotion(seg)} for seg in segments]
