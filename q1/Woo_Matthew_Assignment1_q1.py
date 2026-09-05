#Build an ASCII-to-decimal converter.
import sys

args = sys.argv

print(args)
# s = "Dominic"
s = input("Enter a ASCII word to convert to decimal: ")

#standard
for c in s:
        #print(c, end="," if c != str[-1] else "")
        print(ord(c))

# Pythonic
# print(",".join(str(ord(c)) for c in s))
