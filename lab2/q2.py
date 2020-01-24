"""
Program that inputs a lower bound and upper bound from the user and finds and displays the number and average of all numbers 
between the lower and upper bound (inclusive) that are divisible by 7, but that are not a multiple of 5
"""

num1 = int(input("Enter the lower bound "))
num2 = int(input("Enter the upper bound "))

if num1 > num2:
    print("Invalid range ")
else:
    count = 0
    sum = 0
    for i in range(num1, num2+1):
        if ( (i %  5 != 0) & (i % 7 == 0) ):
            count += 1 
            sum += i

    average = sum / count
    print( " Average is {0:.1f}".format(average))