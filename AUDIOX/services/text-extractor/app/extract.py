import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import os

def extract_text_from_pdf(pdf_path: str, lang: str = "ben+eng") -> str:
    pages = convert_from_path(pdf_path, dpi=300)
    full_text = ""

    for i, page in enumerate(pages):
        text = pytesseract.image_to_string(page, lang=lang)
        full_text += text + "\n\n"
    
    return full_text



# import fitz  # PyMuPDF

# def extract_text_from_pdf(filepath: str) -> str:
#     doc = fitz.open(filepath)
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     doc.close()
#     return text
