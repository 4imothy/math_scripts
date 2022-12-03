from Printing import *
from Strassen import strassen
import numpy as np
import math

def main():
    A = gatherData("A")
    B = gatherData("B")
    a_col = len(A[0])
    a_row = len(A)

    b_col = len(B[0])
    b_row = len(B)
    if a_col != b_row:
        prRed("# Columns of A ≠ # Rows of B")
        exit()

    # check if matrices match the strassen constraints
    if isPowerOfTwo(a_col) and isPowerOfTwo(b_row) and a_col == a_row and b_col == b_row:
        prYellow("Using Strassen")
        ans = strassen(a_row,A,B)
        p = np.matrix([l[0] for l in ans])
        p = np.asarray(ans)
        prPurple("Answer:")
        prLightGray(p)
    else: #use the other method
        ans = multiply(A,B, a_row, b_col)
        prPurple("Answer:")
        print_matrix(ans)

def multiply(A,B, a_row, b_col):
    C = [[0 for i in range(b_col)] for j in range(a_row)]
    for row in range(len(A)):
        for col in range(len(B[0])):
            for elt in range(len(B)):
                C[row][col] += A[row][elt] * B[elt][col]

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
        entries = list(map(float , input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = reshape_list(entries,numCol)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prPurple(name + "=")
    print_matrix(matrix)
    prYellow("------------")
    return matrix

def isPowerOfTwo(num):
    if math.log(num,2).is_integer():
        return True
    else:
        return False

def reshape_list(L, xsize):
    gap = []
    v, r = divmod(len(L),xsize)
    gap = [None]*r
    return list(map(list, zip(*[iter(L+gap)]*xsize)))

def print_matrix(matrix):
        for i in range(0,len(matrix)):
            prLightGray(matrix[i])

if __name__=="__main__":
    main()

