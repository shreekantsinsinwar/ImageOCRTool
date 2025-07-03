import argparse
import logging
import os
from ocr_engine.extractor import extract_text_from_image

# Logging config
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s — %(levelname)s — %(message)s"
)

def save_text_to_file(text: str, output_path: str):
    try:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text)
        logging.info(f"Text saved to {output_path}")
    except Exception as e:
        logging.error(f"Failed to save text: {e}")

def main():
    parser = argparse.ArgumentParser(description="Extract text from an image using OCR.")
    parser.add_argument("image_path", help="Path to the input image file")
    args = parser.parse_args()

    image_path = args.image_path
    text = extract_text_from_image(image_path)

    if text.strip():
        filename = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
        output_file = os.path.join("output", filename)
        os.makedirs("output", exist_ok=True)
        save_text_to_file(text, output_file)
    else:
        logging.warning("No text extracted from the image.")

if __name__ == "__main__":
    main()
