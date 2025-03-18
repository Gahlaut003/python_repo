# import asyncio
from pyppeteer import launch

async def convert_html_to_pdf(html_path, pdf_output_path):
    browser = await launch()
    page = await browser.newPage()
    with open(html_path, 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()

    await page.setContent(html_content)
    await page.waitForSelector('body');
    await page.waitForSelector('table');
    await page.pdf({
        'path': pdf_output_path,
        'format': 'A4',
        'printBackground': True,  
        'margin': {
            'top': '20px',
            'right': '20px',
            'bottom': '20px',
            'left': '20px',
        },
    })

    await browser.close()
html_file_path = "./file.html"
output_pdf_path = "./output51.pdf"
convert_html_to_pdf(html_file_path, output_pdf_path)
print(f"PDF file created at: {output_pdf_path}")
