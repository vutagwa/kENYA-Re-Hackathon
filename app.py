from flask import Flask, request, jsonify, render_template
import os
from ocr_module import extract_text_from_pdf
from data_processing import process_rating_guide, process_proposal_form, process_financial_statements, combine_data
from ai_module import generate_quote
from pdf_generation import generate_pdf

app = Flask(__name__)

# Load the rating guide once at the start
rating_guide = process_rating_guide('C:\\Users\\HP\\OneDrive\\Desktop\\KeReHackathon\\dataSets\\PI - Rating guide.pdf')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle the file upload
    proposal_file = request.files['proposal']
    fs_2023_file = request.files['fs_2023']
    fs_2022_file = request.files['fs_2022']
    
    # Extract text from files
    proposal_text = extract_text_from_pdf(proposal_file)
    fs_2023_text = extract_text_from_pdf(fs_2023_file)
    fs_2022_text = extract_text_from_pdf(fs_2022_file)

    # Process data
    proposal_data = process_proposal_form(proposal_text)
    financial_data_2023 = process_financial_statements(fs_2023_text)
    financial_data_2022 = process_financial_statements(fs_2022_text)

    # Combine all data
    combined_data = combine_data(proposal_data, financial_data_2023)
    combined_data = combine_data(combined_data, financial_data_2022)

    # Generate quote
    premium = generate_quote(combined_data, rating_guide)

    # Prepare response
    response = {
    'premium': premium,
    'details': 'Your estimated premium has been calculated based on provided data.',
    'pdf_url': '/quote.pdf'  
}


    # Generate PDF 
    generate_pdf(response, f"quote.pdf")

    return jsonify(response)

@app.route('/submit-manual', methods=['POST'])
def submit_manual():
    # Extract data from the form
    data = request.form.to_dict()

    # Validate user input
    try:
        estimated_income = float(data['estimated_income'])
        limit_of_indemnity = float(data['limit_of_indemnity'])
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

    # Process the data and generate quotation
    quotation = generate_quotation(data)

    return jsonify(quotation)

def generate_quotation(data):
    estimated_income = float(data['estimated_income'])
    limit_of_indemnity = float(data['limit_of_indemnity'])
    premium = (estimated_income * 0.01) + (limit_of_indemnity * 0.005)

    return {
        'premium': round(premium, 2),
        'details': 'Your estimated premium has been calculated.'
    }

if __name__ == '__main__':
    app.run(debug=True)
