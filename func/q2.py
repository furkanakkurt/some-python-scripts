import math

def isPrime(x):

    for i in range(2, int(math.sqrt(x))+1):
        if ( x % i == 0 ):
            return False
    return True


number = int(input("Enter a number to check whether it is prime or not "))

if isPrime(number):
    print("The number you have entered is prime.")
else:
    print("The number you have entered is not prime.")