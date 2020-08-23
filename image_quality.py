import PIL
from PIL import Image

basewidth = 500
img = Image.open('beautiful-1274361_1920.jpg')

wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
img.save('resized_beautiful-1274361_1920.jpg')