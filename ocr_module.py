import pytesseract
from pdf2image import convert_from_path
import os

def extract_text_from_pdf(pdf_path):
    """
    Extracts text from a PDF file using OCR.
    
    Args:
    pdf_path (str): Path to the PDF file.

    Returns:
    str: Extracted text from the PDF or an error message.
    """
    try:
        # Convert PDF to images
        images = convert_from_path(pdf_path)
        text = ""

        # Iterate through the images and extract text
        for image in images:
            text += pytesseract.image_to_string(image) + "\n"
        
        return text.strip() or "No text found."  # Return a message if no text is extracted

    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return "Error occurred during extraction."
