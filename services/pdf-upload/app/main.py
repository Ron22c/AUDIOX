from fastapi import FastAPI, UploadFile, File, HTTPException
from .storage import upload_pdf
from .publisher import publish_pdf_uploaded_message
from datetime import datetime
from io import BytesIO

app = FastAPI()

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed.")
    
    timestamp = datetime.utcnow().strftime("%Y%m%d-%H%M%S")
    filename = f"{timestamp}-{file.filename}"
    
    contents = await file.read()
    file_url = upload_pdf(BytesIO(contents), filename)
    
    publish_pdf_uploaded_message(file_url, filename, timestamp)

    return {
        "filename": filename,
        "file_url": file_url,
        "uploaded_at": timestamp
    }
