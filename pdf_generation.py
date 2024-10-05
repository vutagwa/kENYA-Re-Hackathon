from fpdf import FPDF

def generate_pdf(data, output_filename):
    """
    Generates a PDF file with the given quotation data.

    Args:
    data (dict): Data to include in the PDF.
    output_filename (str): The filename for the generated PDF.
    """
    pdf = FPDF()
    pdf.add_page()

    # Add content to the PDF
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Premium: {data['premium']}", ln=True)
    pdf.cell(200, 10, txt=data['details'], ln=True)

    # Save the PDF to a file
    pdf.output(output_filename)

