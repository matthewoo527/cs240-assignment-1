#import Image module from Pillow Library
from PIL import Image

#A function called convert, that takes RGB String and convert to a shorter and easier string to read.
def convert(color):
    if color == "(237, 28, 36)":
        return "R"
    elif color == "(0, 0, 0)":
        return "B"
    elif color == "(255, 242, 0)":
        return "Y"
    else:
        return color

#Open a file called "output.txt" in w(write) mode
output_file = open("output.txt", "w")

#Open the image called "smiley.bmp" and load that image
image_file = Image.open("./smiley.bmp")
image_file.load()

#Save the image size to the variable called width and height
width, height = image_file.size

#A forloop that run through each line
for y in range(height):
    #A forloop that run through each pixel of each line
    for x in range(width):
        #Get the pixel of that box that currently at, turn it to a string type and put it in the variable called "color"
        color = str(image_file.getpixel((x,y)))
        #Call the function that we created above, put the results return from the function and save it into the variable "color"
        color = convert(color)
        #Write that color and a space " " after it
        output_file.write(color)
        output_file.write(" ")
    #After it run through each line, write a next line in the "output.txt" file
    output_file.write("\n") #\ = Escape, \\ for \
#Close that output file
output_file.close()