# CS240 Assignment 1
_Author: Matthew Woo_

_Date: Sep 3, 2026_

_[GitHub Repository URL](https://github.com/matthewoo527/cs240-assignment-1/)_

## Converter and Pixel System

### [1. Build an ASCII-to-decimal converter.](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q1/Woo_Matthew_Assignment1_q1.py)
A converter that converts ASCII to decimal.

Screenshot of the output: [q1test.png](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q1/q1test.png)

>Example: When the user enters a string, it will print the decimal value of that string.

### [2. Build a number-base converter supporting binary, decimal, octal, and hexadecimal.](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q2/Woo_Matthew_Assignment1_q2.py)

__Source code file name: [Woo_Matthew_Assignment1_q2.py](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q2/Woo_Matthew_Assignment1_q2.py)__

> #### [Test cases (go to section 5)](https://github.com/matthewoo527/cs240-assignment-1/blob/main/README.md#5-test-boundary-cases-including-zero-the-largest-supported-unsigned-value-and-at-least-one-negative-twos-complement-value)


### [3. Write a program that reads an image and prints its pixel values.](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q3)
__Source code file name: [Woo_Matthew_Assignment1_q3.py](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q3/Woo_Matthew_Assignment1_q3.py)__

__Input file(image): [smiley.bmp](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q3/smiley.bmp)*__

*For the image type I did not use .png because my paint app on win11 automatic use RGBA instead RGB so I use .bmp instead.

__Output file(text): [output.txt](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q3/output.txt)__

I created my own version of smiley, and it is 10px * 10px. It has 3 colors.

Red (R): `rgb(237, 28, 36)`, 
Black (B): `rgb(0, 0, 0)`, 
Yellow (Y): `rgb(255, 242, 0)`

The program takes the image as an input file and outputs a txt file that contains the pixel values of the image.

### [4. Write a program that consumes pixel values and creates an image.](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q4)
__Source code file name: [Woo_Matthew_Assignment1_q4.py](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q4/Woo_Matthew_Assignment1_q4.py)__

__Input file(text): [input.txt](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q4/input.txt)__

__Output file(image): [output.png](https://github.com/matthewoo527/cs240-assignment-1/blob/main/q4/output.png)__



### 5. Test boundary cases, including zero, the largest supported unsigned value, and at least one negative two's-complement value.
#### [Test cases for question 2](https://github.com/matthewoo527/cs240-assignment-1/blob/main/README.md#2-build-a-number-base-converter-supporting-binary-decimal-octal-and-hexadecimal)

* #### __Boundary cases__
  ```
  Enter a number: 10
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: d
  Which base to convert to? [b/d/o/h] b
  From base: decimal, To base: binary, Result: 1010
  ```
  ```
  Enter a number: 1010
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: b
  Which base to convert to? [b/d/o/h] d
  From base: binary, To base: decimal, Result: 10
  ```
  ```
  Enter a number: 10
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: d
  Which base to convert to? [b/d/o/h] o
  From base: decimal, To base: octal, Result: 12
  ```
  ```
  Enter a number: 12
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: o
  Which base to convert to? [b/d/o/h] d
  From base: octal, To base: decimal, Result: 10
  ```
  ```
  Enter a number: 255
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: d
  Which base to convert to? [b/d/o/h] h
  From base: decimal, To base: hexadecimal, Result: ff
  ```
  ```
  Enter a number: ff
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: h
  Which base to convert to? [b/d/o/h] d
  From base: hexadecimal, To base: decimal, Result: 255
  ```
  ```
  Enter a number: 1010
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: b
  Which base to convert to? [b/d/o/h] h
  From base: binary, To base: hexadecimal, Result: a
  ```
  ```
  Enter a number: a
  Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: h
  Which base to convert to? [b/d/o/h] b
  From base: hexadecimal, To base: binary, Result: 1010
  ```

* #### __Including zero__

* #### __The largest supported unsigned value__

* #### __Negative two's-complement value.__
