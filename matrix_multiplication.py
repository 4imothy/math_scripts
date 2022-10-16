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
print("A: ")
prLightGray(A)

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
print("B: ")
prLightGray(B)

result = []
# iterating by row of A
for i in range(len(A)):

    # iterating by column by B
    for j in range(len(B[0])):

        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)
