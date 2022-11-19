from Printing import *
import numpy as np

def main():
    A = gatherData()
    try:
        det = determinant(A)
    except:
        prPurple("The Determinant Is: 0")
        exit()
    prPurple("The Determinant Is: ")
    prLightGray(abs(det))

def determinant(A):
    # Section 1: Establish n parameter and copy A
    n = len(A)

    # Section 2: Row ops on A to get in upper triangle form
    for fd in range(n): # A) fd stands for focus diagonal
        for i in range(fd+1,n): # B) only use rows below fd row
            if A[fd][fd] == 0: # C) if diagonal is zero ...
                A[fd][fd] = 1.0e-18 # change to ~zero
            # D) cr stands for "current row"
            crScaler = A[i][fd] / A[fd][fd]
            # E) cr - crScaler * fdRow, one element at a time
            for j in range(n):
                A[i][j] = A[i][j] - crScaler * A[fd][j]

    # Section 3: Once AM is in upper triangle form ...
    product = 1.0
    for i in range(n):
        # ... product of diagonals is determinant
        product *= A[i][i]

    return product

def gatherData():
    prPurple("Enter Matrix")
    try:
        numRow = int(input(makeCyan("Enter the number of rows: ")))
        numCol = int(input(makeCyan("Enter the number of columns: ")))
        if numCol != numRow:
            prRed("Matrix is not square: 0")
            exit()
    except:
        prRed("That is not a number")
        exit()
    if numRow != numCol:
        prRed("Not a square matrix")
        exit()
    try:
        entries = list(map(np.double, input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = np.array(entries).reshape(numRow, numCol)
    except:
        prRed("Matrix is not properly formatted")
        exit()
    prPurple("Matrix=")
    prLightGray(matrix)
    return matrix

if __name__ == "__main__":
    main()
