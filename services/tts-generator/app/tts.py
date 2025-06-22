import os
from TTS.api import TTS

# Load a multilingual model (with Bengali support)
tts_model = TTS(model_name="tts_models/hi/tacotron2-DDC", progress_bar=False)

def synthesize(text: str, filename: str, emotion: str = "neutral") -> str:
    os.makedirs("/tmp/audio", exist_ok=True)
    filepath = f"/tmp/audio/{filename}.wav"

    # Coqui doesn’t support emotion control directly, so we simulate by adjusting speaker embeddings (future)
    tts_model.tts_to_file(text=text, file_path=filepath)

    return filepath
