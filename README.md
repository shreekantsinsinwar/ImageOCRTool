# 🖼️ ImageOCRTool — Extract Text from Images with One Command

A simple yet powerful Python CLI tool to extract text from images using **Tesseract OCR**.

Built for:
- 🧠 Developers who work with image-based data  
- 📂 Anyone tired of manually copying text from screenshots  
- 🛠️ Automating workflows like invoice extraction, document parsing, etc.

---

## 🚀 Features

✅ Command-line usage  
✅ Works on Linux and macOS  
✅ Supports `.png`, `.jpg`, `.jpeg` formats  
✅ Extracts and saves text to `.txt` automatically  
✅ Built with Python, Pillow, Tesseract & argparse  

---

## 📸 Sample Use Case

Say you have this file:

```bash
images/sample_invoice.png


## Just run:

  python main.py images/sample_invoice.png

## And boom! You’ll get a .txt file inside the output/ folder like this:

  output/sample_invoice.txt

🔧 Setup Instructions

    Clone this repository

git clone https://github.com/shreekantsinsinwar/ImageOCRTool.git
cd ImageOCRTool

    Install Python dependencies

pip install -r requirements.txt

    Install Tesseract OCR engine

# For Ubuntu/Debian
sudo apt install tesseract-ocr

# For Mac (via Homebrew)
brew install tesseract