import sys
# Program to multiply two matrices using nested loopsO

if len(sys.argv) < 3:
    print(f'\033[91mNot Enough Parameters\033[0m')
    exit()

A = [];

for i in sys.argv[1]:
    print(i)

# take a 3x4 matrix
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

# iterating by row of A
for i in range(len(A)):

    # iterating by column by B
    for j in range(len(B[0])):

        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)
