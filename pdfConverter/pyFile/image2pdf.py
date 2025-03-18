from PIL import Image

image_1 = Image.open(r'1.jpg')
image_2 = Image.open(r'2.jpg')
image_3 = Image.open(r'3.jpg')
image_4 = Image.open(r'4.jpg')

im_1 = image_1.convert('RGB')
im_2 = image_2.convert('RGB')
im_3 = image_3.convert('RGB')
im_4 = image_4.convert('RGB')

image_list = [im_2, im_3, im_4]

im_1.save(r'./des/images.pdf', save_all=True, append_images=image_list)