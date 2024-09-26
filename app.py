from flask import Flask, request, jsonify, render_template
import os
import pandas as pd
from ocr_module import extract_text_from_pdf
from data_processing import process_rating_guide, process_proposal_form, process_financial_statements, combine_data
from ai_module import generate_quote
from pdf_generation import generate_pdf

app = Flask(__name__)

# Load the rating guide once at the start
try:
    rating_guide = process_rating_guide('dataSets/PI - Rating guide.xlsx')
except Exception as e:
    print(f"Error loading rating guide data: {e}")
    rating_guide = None  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Check if files were uploaded
    if 'proposal' not in request.files or 'fs_2023' not in request.files or 'fs_2022' not in request.files:
        return jsonify({'error': 'Missing file(s)'}), 400

    # Save uploaded files
    proposal_file = request.files['proposal']
    fs_2023_file = request.files['fs_2023']
    fs_2022_file = request.files['fs_2022']
    
    try:
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
            'details': 'Your estimated premium has been calculated based on provided data.'
        }

        # Generate PDF
        generate_pdf(response, f"quote.pdf")

        return jsonify(response)

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        return jsonify({'error': 'An error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)
