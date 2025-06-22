from gtts import gTTS
from pydub import AudioSegment
import os

AUDIO_DIR = "/tmp/audio"

def synthesize(text: str, filename: str, lang="bn") -> str:
    os.makedirs(AUDIO_DIR, exist_ok=True)
    file_path = f"{AUDIO_DIR}/{filename}.mp3"

    tts = gTTS(text=text, lang=lang)
    tts.save(file_path)

    return file_path


def combine_audio_segments(filename: str, segment_count: int) -> str:
    combined = AudioSegment.empty()

    for i in range(segment_count):
        seg_path = f"{AUDIO_DIR}/{filename}-seg{i}.mp3"
        if os.path.exists(seg_path):
            audio = AudioSegment.from_mp3(seg_path)
            combined += audio
        else:
            print(f"[TTS] Missing segment: {seg_path}")

    final_path = f"{AUDIO_DIR}/{filename}_final.mp3"
    combined.export(final_path, format="mp3")
    print(f"[TTS] Final combined audio saved: {final_path}")
    return final_path
