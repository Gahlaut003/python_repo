from xhtml2pdf import pisa

def html_file_to_pdf(html_file_path, pdf_output_path):
    # Read HTML content from file
    with open(html_file_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Convert HTML to PDF using pisa
    with open(pdf_output_path, 'wb') as pdf_file:
        options = {
            'media': 'print',  # Specify print media type
        }
        pisa.CreatePDF(html_content, dest=pdf_file, options=options)

# Example HTML file path
html_file_path = "file.html"

# Convert HTML to PDF
output_pdf_path = "output3.pdf"
html_file_to_pdf(html_file_path, output_pdf_path)

print(f"PDF file created at: {output_pdf_path}")
