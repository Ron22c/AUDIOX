from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from .minio_utils import list_audio_files, get_audio_stream

app = FastAPI()

@app.get("/stories")
def list_stories():
    files = list_audio_files()
    return {"stories": [f for f in files if f.endswith("_final.mp3")]}

@app.get("/stories/{story_id}")
def stream_story(story_id: str):
    filename = f"{story_id}_final.mp3"
    try:
        audio_data = get_audio_stream(filename)
        return StreamingResponse(audio_data, media_type="audio/mpeg")
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
