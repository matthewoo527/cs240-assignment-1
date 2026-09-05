# CS240 assignment 1
_Author: Matthew Woo_

_Date: Sep 3, 2026_

_[Github Repositories](https://github.com/matthewoo527/cs240-assignment-1/)_

## Converter and Pixel System

### 1. Build an ASCII-to-decimal converter.

### 2. Build a number-base converter supporting binary, decimal, octal, and hexadecimal.

### 3. Write a program that reads an image and prints its pixel values.
__File name: [Woo_Matthew_Assignment1_q3.py](https://github.com/matthewoo527/cs240-assignment-1/blob/main/Woo_Matthew_Assignment1_q3.py)__

__Input file(image): [smiley.bmp](https://github.com/matthewoo527/cs240-assignment-1/blob/main/smiley.bmp)__
_For the image type I did not use .png because my paint app on win11 automatic use RGBA instead RGB so I use .bmp instead_

__Output file(text): [output.txt](https://github.com/matthewoo527/cs240-assignment-1/blob/main/output.txt)__

I created my own version of smiley, and it is 10px * 10px. It has 3 colors.

Red (R): `rgb(237, 28, 36)`, 
Black (B): `rgb(0, 0, 0)`, 
Yellow (Y): `rgb(255, 242, 0)`

The program takes the image as an input file and outputs a txt file that contains the pixel values of the image.

### 4. Write a program that consumes pixel values and creates an image.

### 5. Test boundary cases, including zero, the largest supported unsigned value, and at least one negative two's-complement value.
