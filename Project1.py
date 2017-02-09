#https://github.com/jantongiovanni/205proj1
#Joe Antongiovanni
#2/9/17
#Purpose: takes median pixel values of all images to form new image
from PIL import Image #imports PIL library

myList = [] #empty list to store images

for x in range(1,10):  #opens all images
    myList.append(Image.open(str(x) + '.png'))
    
width, height = myList[0].size #stores image size to be used for new image

im = Image.new("RGB", (width, height)) #creates new RGB image 

R = [0]*9 #RGB arrays to store color values for all pixels
G = [0]*9
B = [0]*9

for x in range(width): #loops through horizontal pixels
    for y in range(height): #loops through vertical pixels
        for z in range(0,9): #loops through images
             R[z], G[z], B[z] = myList[z].getpixel((x, y)) #stores RGB value for every pixel in all images
        R.sort() #sorts RGB values
        G.sort()
        B.sort()
        im.putpixel((x,y),(R[4], G[4], B[4])) #places median RGB pixel value in new image

im.save("Final_Image.png") #saves new image
