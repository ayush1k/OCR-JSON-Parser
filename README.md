# OCR-JSON-Parser

initial commands --
pip install requirements.txt

---

# 📄 OCR-to-JSON Parser CLI Tool

This is a simple command-line tool that extracts text from **images** or **PDF documents** using OCR (Optical Character Recognition) and returns the extracted content in clean **JSON format**.

---

## 🚀 Features

- 📤 Accepts **image** (`.jpg`, `.png`) or **PDF** files as input
- 🔍 Extracts text using `Tesseract OCR`
- 📦 Outputs structured **JSON**
- 🧠 Supports multi-page PDF processing
- ⚙️ Lightweight and easy to use from terminal

---

## 🛠️ Tech Stack

- 🐍 Python 3
- 🧠 [pytesseract](https://pypi.org/project/pytesseract/)
- 📷 [Pillow (PIL)](https://pypi.org/project/Pillow/)
- 📄 [pdf2image](https://pypi.org/project/pdf2image/)
- 📌 Tesseract OCR (must be installed on your system)
- 🧾 Poppler (for converting PDF to images)

---

## 📁 Folder Structure

OCR-to-JSON/
│
├── ocr_to_json.py # Main Python script
├── sample.png # Sample test image
├── sample.pdf # (Optional) Sample test PDF
├── README.md # Project documentation
└── requirements.txt # Dependency list



---

## 🧑‍💻 How It Works

### ✅ Step 1: User runs the script with a file path


python ocr_to_json.py sample_image.jpg
✅ Step 2: Script detects if file is image or PDF
✅ Step 3: Uses pytesseract to extract text
✅ Step 4: Text is wrapped in a JSON object and printed (or optionally saved)
📥 Installation Guide
🔧 Install Python dependencies
bash
Copy
Edit
pip install pytesseract pdf2image Pillow
🔧 Install Tesseract OCR
➤ Windows
Download from: https://github.com/tesseract-ocr/tesseract

Install and set the path in the script:

python
Copy
Edit
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
➤ Linux
bash
Copy
Edit
sudo apt update
sudo apt install tesseract-ocr poppler-utils
➤ macOS
bash
Copy
Edit
brew install tesseract poppler
🔧 Install Poppler (For PDF support)
Poppler for Windows

Extract it and add the bin/ folder to your system PATH

📝 Usage
For an image:
python ocr_to_json.py sample_ocr_image.png

For a PDF:
python ocr_to_json.py sample.pdf

The output will be:

json
Copy
Edit
{
    "extracted_text": "Name: Ayush Kumar\nDOB: 25 Sep 2005\nCourse: BTech in CSE\nCollege: Rajkiya Engineering College, Kannauj"
}
💡 Optional Enhancements
🔹 Add option to save JSON output to file

🔹 Add language selection for OCR

🔹 Preprocess image (grayscale, thresholding) for better accuracy

🔹 Add GUI using Tkinter or web interface using Flask

🧪 Sample Image for Testing
You can use the included file: sample_ocr_image.png

It contains:


Name: Ayush Kumar
DOB: 25 Sep 2005
Course: BTech in CSE
College: Rajkiya Engineering College, Kannauj
🧾 License
This project is open-source and free to use.

✍️ Author
Ayush Kumar