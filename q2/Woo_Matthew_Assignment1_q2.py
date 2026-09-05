#A number-base converter

#Ask for number and which base this is
number = input("Enter a number: ")
convert_from_base = input("Which base is this number? Binary, decimal, octal, or hexadecimal [b/d/o/h]: ")
convert_to_base = input("Which base to convert to? [b/d/o/h] ")


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

#The convert part, convert the num to the base that the user ask for and save it to the variable "result"
if convert_to_base == "b" or convert_to_base == "B":
    result = bin(num)[2:] #The "[2:]" takes the integer after index 2, since the integer in index 0 and 1 are the decimal type(0b, 0o, 0x)
elif convert_to_base == "d" or convert_to_base == "D":
    result = num #Use num because num is already in decimal
elif convert_to_base == "o" or convert_to_base == "O":
    result= oct(num)[2:]
elif convert_to_base == "h" or convert_to_base == "H":
    result = hex(num)[2:]
else:
    print("Invalid Base")

print("From base: " + print_from_base + ", To base: " + print_to_base + ", Result: " + str(result))
