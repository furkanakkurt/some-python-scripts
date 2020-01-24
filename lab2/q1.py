str = ""

inStr = input("Enter a string ")

if len(inStr) < 2:
    str = inStr*2 + "!!"
else:
    str = inStr[0] + inStr[1] + inStr[-2] + inStr[-1]

print(str)