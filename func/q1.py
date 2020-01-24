"""
Creates an mxn matrix, each element being either 0 or 1, generated randomly. 
"""
import random as r

def generateMatrix(m,n):
    for i in range (1,m+1):
        for j in range (1,n+1):
            rand = r.randint(0,1)
            print(rand, end=" ")
        print()


row = int(input("Enter the row number of the matrix "))
column = int(input("Enter the column number of the matrix "))

generateMatrix(row, column)



