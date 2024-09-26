import pandas as pd

def generate_quote(processed_data, rating_guide):
    estimated_income = processed_data['estimated_income']
    limit_of_indemnity = processed_data['limit_of_indemnity']
    
    # Implement rules based on rating guide
    premium_rate = rating_guide.loc[rating_guide['Limit'] >= limit_of_indemnity, 'Rate'].values[0]
    premium = (estimated_income * premium_rate) + (limit_of_indemnity * 0.005)
    
    return round(premium, 2)
