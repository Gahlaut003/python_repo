import asyncio
from pyppeteer import launch

async def convert_html_to_pdf(html_path, pdf_output_path):
    browser = await launch()
    page = await browser.newPage()

    # Read HTML content from file
    with open(html_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    # Set content to the HTML
    await page.setContent(html_content)

    # Generate PDF from the page content
    await page.pdf({'path': pdf_output_path, 'format': 'A4'})

    await browser.close()

# Example HTML file path
html_file_path = "./file.html"

# Convert HTML to PDF
output_pdf_path = "output.pdf"

# Run the event loop to execute the conversion
asyncio.get_event_loop().run_until_complete(convert_html_to_pdf(html_file_path, output_pdf_path))

print(f"PDF file created at: {output_pdf_path}")
