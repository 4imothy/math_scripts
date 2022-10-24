from Printing import *
from Strassen import strassen
import numpy as np
import math

def main():
    A = gatherData("A")
    B = gatherData("B")
    if A.shape[1] != B.shape[0]:
        prRed("# Columns of A ≠ # Rows of B")
        exit()

    # check if matrices match the strassen constraints
    if isPowerOfTwo(A.shape[1]) and isPowerOfTwo(B.shape[1]) and A.shape[1]==A.shape[0] and B.shape[1]==B.shape[0]:
        print("Using Strassen")
        ans = strassen(A,B)
    else:
        ans = multiply(A,B)

    prPurple("Answer:")
    prLightGray(ans)

def multiply(A,B):

    C = np.zeros((A.shape[0],B.shape[1]),dtype = np.double)
    for row in range(len(A)):
        for col in range(len(B[0])):
            for elt in range(len(B)):
                C[row, col] += A[row, elt] * B[elt, col]

    return C

def gatherData(name):
    prPurple("Matrix " + name)
    try:
        numRow = int(input(makeCyan("Enter the number of rows: ")))
        numCol = int(input(makeCyan("Enter the number of columns: ")))
    except:
        prRed("That is not a number")
        exit()
    try:
        entries = list(map(np.double, input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = np.array(entries).reshape(numRow, numCol)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prPurple(name + "=")
    prLightGray(matrix)
    prYellow("------------")
    return matrix

def isPowerOfTwo(num):
    if math.log(num,2).is_integer():
        return True
    else:
        return False

if __name__=="__main__":
    main()

