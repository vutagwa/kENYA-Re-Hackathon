from flask import Flask, request, render_template, jsonify
import pandas as pd
import numpy as np
import nltk

app = Flask(__name__)

# Load data (you can enhance this with actual data processing)
try:
    rating_guide = pd.read_excel('data/pi_rating_guide.xlsx')
except Exception as e:
    print(f"Error loading rating guide data: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from the form
    data = request.form.to_dict()
    
    # Validate user input
    try:
        estimated_income = float(data['estimated_income'])
        limit_of_indemnity = float(data['limit_of_indemnity'])
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400

    # Process the data
    try:
        quotation = generate_quotation(data)
        return jsonify(quotation)
    except Exception as e:
        return jsonify({'error': 'An error occurred'}), 500

def generate_quotation(data):
    estimated_income = float(data['estimated_income'])
    limit_of_indemnity = float(data['limit_of_indemnity'])
    premium = (estimated_income * 0.01) + (limit_of_indemnity * 0.005)  

    return {
        'premium': round(premium, 2),
        'details': 'Your estimated premium has been calculated.'
    }

if __name__ == '__main__':
    app.run(debug=False)