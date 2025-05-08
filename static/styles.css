import pytesseract
from pdf2image import convert_from_path
import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    if not text.strip():
        # OCR fallback
        images = convert_from_path(pdf_path)
        for img in images:
            text += pytesseract.image_to_string(img, lang='hin')
    return text
