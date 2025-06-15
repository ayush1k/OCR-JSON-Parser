import pytesseract
from PIL import Image
import json
import sys
import os
from pdf2image import convert_from_path

# Set this to your Tesseract path (only on Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    images = convert_from_path(pdf_path)
    all_text = ''
    for i, img in enumerate(images):
        text = pytesseract.image_to_string(img)
        all_text += f"\n--- Page {i+1} ---\n{text}"
    return all_text

def to_json(text):
    return json.dumps({"extracted_text": text}, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ocr_to_json.py <image_or_pdf_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print("File not found.")
        sys.exit(1)

    if file_path.lower().endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_image(file_path)

    json_output = to_json(text)
    print(json_output)
