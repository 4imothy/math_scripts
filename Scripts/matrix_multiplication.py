from Printing import *
import numpy as np

def gatherData(name):
    prLightPurple("Matrix " + name)
    numRow = int(input(makeCyan("Enter the number of rows: ")))
    numCol = int(input(makeCyan("Enter the number of columns: ")))
    try:
        entries = list(map(int, input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = np.array(entries).reshape(numRow, numCol)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prLightPurple(name + ": ")
    prLightGray(matrix)
    print("------------")
    return matrix

A = gatherData("A")
B = gatherData("B")
if A.shape[1] != B.shape[0]:
        prRed("# Columns of A ≠ # Rows of B")
        exit()

C = np.zeros((A.shape[0],B.shape[1]),dtype = int)

for row in range(len(A)):
    for col in range(len(B[0])):
        for elt in range(len(B)):
            C[row, col] += A[row, elt] * B[elt, col]

prPurple("Answer:")
prLightGray(C)
