#Import image module from the pillow library
from PIL import Image

#A function called color that convert the string to RGB value
def convert(color):
    if color == "R":
        return (237, 28, 36)
    elif color == "B":
        return (0, 0, 0)
    elif color == "Y":
        return (255, 242, 0)
    else:
        return color

#Open "input.txt" in r(read) mode
input_text_file = open("input.txt", "r")

lines = input_text_file.readlines()

width, height = lines[0].count(" "), len(lines)

output_image_file = Image.new("RGB", (width, height))

#A forloop statement that go through every line
for y in range(height):
    #Assign the current line to the variable "line"
    line = lines[y]
    #Split each line to lists
    pixels = line.split()
    #A forloop statement that go through the pixel of each line
    for x in range(width):
        #Call the "convert" function to convert the string to RGB
        pixel = convert(pixels[x])
        #Put the pixels into the output image file
        output_image_file.putpixel((x,y), pixel)

#Save the image as "output.png"
output_image_file.save("output.png")

#Close the input text and output image file
input_text_file.close()
output_image_file.close()
