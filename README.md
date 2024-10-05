# Indemnity Quotation System
 This is an AI-powered web application designed to help users calculate insurance premiums based on their financial information. Users can upload relevant documents or enter data manually to receive a generated quote, including a downloadable PDF of the quotation details.

## Features
File Upload: Users can upload a proposal form and financial statements for 2022 and 2023.
Manual Entry: Users have the option to enter estimated income and limit of indemnity directly via a form.
OCR Data Extraction: The application uses Tesseract OCR to extract text from uploaded PDF documents.
Premium Calculation: Premiums are calculated based on a rating guide.
PDF Generation: Users receive a downloadable PDF containing the calculated premium and relevant details.

## Technologies Used
Flask: Web framework for Python to handle web requests and serve content.
Pandas: For data manipulation and processing.
Tesseract OCR: To extract text from PDF files.
PDF Generation: Utilizes FPDF to create PDF documents.
HTML/CSS: For the front-end user interface.

## Installation
### Prerequisites
Python 3.12.4
Flask
Pandas
Tesseract OCR
pytesseract
pdf2image
fpdf

## Steps to Install
1. Clone the repository:
        git clone <repository-url>
        cd keReHackathon
2. Create a virtual environment:
        python -m venv venv
        source venv/bin/activate
3. Install required packages:
        pip install -r requirements.txt
## Usage
Start the Flask application:
        python app.py
        Open your web browser and navigate to http://127.0.0.1:5000/.

Uploading Documents:

Use the file upload section to select and upload the proposal form and financial statements.
Alternatively, fill out the manual entry form with the estimated income and limit of indemnity.
After submission, the system will calculate the premium and provide a downloadable PDF link with the quote.

### Folder Structure
/KEREHACKATHON
│
├── /static                 # Folder for static files 
│
├── /datasets               # Folder for the datasets
│
├── /templates              # Folder for HTML templates
│
├── app.py                  # Main application file
├── data_processing.py      # Module for data processing functions
├── ocr_module.py           # Module for OCR functionality
├── pdf_generation.py       # Module for PDF generation
└── requirements.txt        # List of required packages

## License
This project is licensed under the MIT License.

