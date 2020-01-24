"""
Creates and displays a string made of the first 2 and the last 2 chars of a given a string. 
If the string length is less than 2, the extra spaces are the ! character
"""
str = ""

inStr = input("Enter a string ")

if len(inStr) < 2:
    str = inStr*2 + "!!"
else:
    str = inStr[0] + inStr[1] + inStr[-2] + inStr[-1]

print(str)