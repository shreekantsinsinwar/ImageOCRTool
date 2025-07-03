from PIL import Image
import pytesseract
import logging
import os

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from the image at the given path using OCR.
    """
    if not os.path.exists(image_path):
        logging.error(f"File not found: {image_path}")
        return ""

    try:
        logging.info(f"Opening image: {image_path}")
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img)
        logging.info(f"Text extracted successfully.")
        return text
    except Exception as e:
        logging.error(f"Error while processing image: {e}")
        return ""
