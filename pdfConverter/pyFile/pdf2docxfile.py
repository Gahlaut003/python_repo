# from pdf2docx import parse
# from typing import Tuple


# def convert_pdf2docx(input_file: str, output_file: str, pages: Tuple = None):
#     """Converts pdf to docx"""
#     if pages:
#         pages = [int(i) for i in list(pages) if i.isnumeric()]
#     result = parse(pdf_file=input_file,
#                    docx_with_path=output_file, pages=pages)
#     summary = {
#         "File": input_file, "Pages": str(pages), "Output File": output_file
#     }
#     # Printing Summary
#     print("## Summary ########################################################")
#     print("\n".join("{}:{}".format(i, j) for i, j in summary.items()))
#     print("###################################################################")
#     return result


# if __name__ == "__main__":
#     import sys
#     input_file = sys.argv[1]
#     output_file = sys.argv[2]
#     convert_pdf2docx('./src/Abhishek_resume_2.pdf', './src/Abhi2.docx')   



# import PyPDF2

# path="../des/spidy.pdf "
# text=""
# pdf_file = open(path, 'rb')
# text =""
# # pdf_reader = PdfFileReader(input_file,strict=False)
# read_pdf = PyPDF2.PdfFileReader(pdf_file,strict=False)
# c = read_pdf.numPages
# for i in range(c):
#      page = read_pdf.getPage(i)
#      text+=(page.extractText())



import aspose.words as aw

# load the PDF file
doc = aw.Document("../des/images.pdf")

# convert PDF to Word DOCX format
doc.save("../des/pdf-to-word.docx")



# from pdf2docx import Converter

# pdf_file = '../des/images.pdf'
# docx_file = '../des/sample.docx'

# # convert pdf to docx
# cv = Converter(pdf_file)
# cv.convert(docx_file)      # all pages by default
# cv.close()



# from pdf2docx import parse

# pdf_file = '../des/images.pdf'
# docx_file = '../des/sample.docx'

# # convert pdf to docx
# parse(pdf_file, docx_file)