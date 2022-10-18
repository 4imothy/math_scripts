from Printing import *
import numpy as np

# get matrix A
prLightPurple("Matrix A")
RA = int(input("Enter the number of rows: "))
CA = int(input("Enter the number of columns: "))
prCyan("Enter the entries in a single line (separated by space): ")
entriesA = list(map(int, input().split()))
try:
    A = np.array(entriesA).reshape(RA, CA)
except:
    prRed("A is not properly formatted")
    exit()
prLightPurple("A: ")
prLightGray(A)

print("----------")
# set matrix B
prLightPurple("Matrix B")
RB = int(input("Enter the number of rows: "))
if CA != RB:
    prRed("# Columns of A ≠ # Rows Of B")
    exit()
CB = int(input("Enter the number of columns: "))
prCyan("Enter the entries in a single line (separated by space): ")
entriesB = list(map(int, input().split()))
try:
    B = np.array(entriesB).reshape(RB, CB)
except:
    prRed("B is not properly formatted")
    exit()
prLightPurple("B: ")
prLightGray(B)

C = np.zeros((A.shape[0],B.shape[1]),dtype = int)
for row in range(len(A)):
    for col in range(len(B[0])):
        for elt in range(len(B)):
            C[row, col] += A[row, elt] * B[elt, col]

print("----------")
prPurple("Answer:")
prLightGray(C)
