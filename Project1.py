#print "Hello World"

from PIL import Image
image = Image.open('1.png')
width, height = image.size
print width
print height
pixel_values = list(image.getdata())
#return pixel_values

pic = image.load()
print pic[0,0]
#comment