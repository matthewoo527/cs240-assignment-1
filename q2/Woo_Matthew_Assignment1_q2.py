#A number-base converter

#AI Disclose usage:
#I asked ChatGPT what to change in the code,
#and learned what is the difference between
#signed and usigned 8 bits.
#So it can pass the negative two's complement case.

#Ask for number and which base this is
number = input("Enter a number: ")
convert_from_base = input("Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: ")
convert_to_base = input("Which base to convert to? [b/d/o/h] ")

#Bit Size for negative two's complement
BIT_SIZE = 8

#This if statement is for printing the result, from base
print_from_base = "invalid base"
if convert_from_base == "b" or convert_from_base == "B":
    print_from_base = "binary"
elif convert_from_base == "d" or convert_from_base == "D":
    print_from_base = "decimal"
elif convert_from_base == "o" or convert_from_base == "O":
    print_from_base = "octal"
elif convert_from_base == "h" or convert_from_base == "H":
    print_from_base = "hexadecimal"
else:
    print("Invalid Base")

#This if statement is for printing the result, to base
print_to_base = "invalid base"
if convert_to_base == "b" or convert_to_base == "B":
    print_to_base = "binary"
elif convert_to_base == "d" or convert_to_base == "D":
    print_to_base = "decimal"
elif convert_to_base == "o" or convert_to_base == "O":
    print_to_base = "octal"
elif convert_to_base == "h" or convert_to_base == "H":
    print_to_base = "hexadecimal"
else:
    print("Invalid Base")

#Set the base to an int so the int function can take it as the parameter
if convert_from_base == "b" or convert_from_base == "B":
    convert_from_base = 2
elif convert_from_base == "d" or convert_from_base == "D":
    convert_from_base = 10
elif convert_from_base == "o" or convert_from_base == "O":
    convert_from_base = 8
elif convert_from_base == "h" or convert_from_base == "H":
    convert_from_base = 16
else:
    print("Invalid Base")

#It takes a str and int base and return a interger of that base
num = int(number, convert_from_base)

#AI Disclose: Inspired by ChatGPT
#It checks if the number fits 8 bits
#and convert the negative number to 8 bit two's complement
#It can handle the negative two's complement case too.

#Unsiged: 0 to 255
#Signed: -128 to 127
#This code can handle both cases

if num > 255 or num < -128: #From -128 to -1 and 0 to 255
    print("Number is not in 8 bit range")
    exit()
if num < 0:
    converted_num = num + (2 ** BIT_SIZE) #num + 2^8, turns negative decimal to two's complement
else:
    converted_num = num

#The convert part, convert the num to the base that the user ask for and save it to the variable "result"
if convert_to_base == "b" or convert_to_base == "B":
    result = bin(converted_num)[2:] #The "[2:]" takes the integer after index 2, since the integer in index 0 and 1 are the decimal type(0b, 0o, 0x)
    if num < 0: #In the case of negative number, fill zeros on the left for the result
        result = result.zfill(BIT_SIZE) #it fill zeros on the left
elif convert_to_base == "d" or convert_to_base == "D":
    result = num #Use num because num is already in decimal
elif convert_to_base == "o" or convert_to_base == "O":
    result= oct(converted_num)[2:]
elif convert_to_base == "h" or convert_to_base == "H":
    result = hex(converted_num)[2:]
else:
    print("Invalid Base")

print("From base: " + print_from_base + ", To base: " + print_to_base + ", Result: " + str(result))