from reportlab.pdfgen import canvas

def html_to_pdf(html_content, pdf_output_path):
    c = canvas.Canvas(pdf_output_path)
    c.drawString(72, 800, html_content)
    c.save()

html_content = 'file.'
pdf_output_path = 'output211.pdf'
html_to_pdf(html_content, pdf_output_path)
