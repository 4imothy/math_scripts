def submatrices(n, matrix): # dividing matrix for pieces
    A = [[j for j in matrix[i][:int(n / 2)]] for i in range(int(n / 2))]
    B = [[j for j in matrix[i][int(n / 2):]] for i in range(int(n / 2))]
    C = [[j for j in matrix[i][:int(n / 2)]] for i in range(int(n / 2), n)]
    D = [[j for j in matrix[i][int(n / 2):]] for i in range(int(n / 2), n)]
    return [A, B, C, D]


def addition(n, matrix1, matrix2):  # just addition
    res = [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(n)]
    return res

def subtraction(n, matrix1, matrix2):   # just substraction
    res = [[matrix1[i][j] - matrix2[i][j] for j in range(n)] for i in range(n)]
    return res

def strassen(n, matrix1, matrix2):

    if n == 2:  # the last step of algorithm is just standart multiplycation
        xy = [[0] * n for i in range(n)]
        for i in range(n):
            for j in range(n):
                for x in range(n):
                    xy[i][j] += matrix1[i][x] * matrix2[x][j]
    else:
        A, B, C, D = submatrices(n, matrix1)    # divide the original matrix1
        E, F, G, H = submatrices(n, matrix2)    # divide the original matrix2

        n = int(n / 2)  # the matrix size is changed now

        p1 = strassen(n, A, subtraction(n, F, H))
        p2 = strassen(n, addition(n, A, B), H)
        p3 = strassen(n, addition(n, C, D), E)
        p4 = strassen(n, D, subtraction(n, G, E))
        p5 = strassen(n, addition(n, A, D), addition(n, E, H))
        p6 = strassen(n, subtraction(n, B, D), addition(n, G, H))
        p7 = strassen(n, subtraction(n, A, C), addition(n, E, F))

        xy1 = addition(n, addition(n, p5, p6), subtraction(n, p4, p2))  # making new blocks of matrix
        xy2 = addition(n, p1, p2)
        xy3 = addition(n, p3, p4)
        xy4 = subtraction(n, addition(n, p1, p5), addition(n, p3, p7))

        xy = [xy1[i] + xy2[i] for i in range(n)] + [xy3[i] + xy4[i] for i in range(n)]  # assembling a matrix of blocks
    return xy
