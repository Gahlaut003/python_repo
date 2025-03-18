#1st method
# from PIL import Image

# path = './1.jpg'
# pdf = Image.open(path)
# pdf.save('./spidy.pdf')

#2nd method

import img2pdf

with open("./spidy.pdf",'wb') as f:
    f.write(img2pdf.convert('./1.jpg'))
