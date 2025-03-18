import PyPDF2

def compress_pdf(input_pdf_path, output_pdf_path):
    pdf_writer = PyPDF2.PdfFileWriter()
    
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        
        # Iterate through each page and copy it to the output PDF
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            page.compressContentStreams()  # Apply compression
            pdf_writer.addPage(page)
            
        # Write the compressed PDF to a new file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)

if __name__ == "__main__":
    input_pdf_path = "file.pdf"  # Replace with the path to your input PDF
    output_pdf_path = "compre.pdf"  # Path for the compressed PDF
    
    compress_pdf(input_pdf_path, output_pdf_path)
    
    print(f"Compressed PDF saved to: {output_pdf_path}")
