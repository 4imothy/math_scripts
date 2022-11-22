from Printing import *

def main():
    M = gatherData("Matrix")
    # create identity matrix to operate on
    prPurple("Inverse Matrix=")
    try:
        inv = inverse(M)
    except:
        prRed("Not Invertible")
        exit()
    for i in range(0,len(inv)):
        prLightGray(inv[i])

def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                prRed("Matrix is not invertible")
                exit()
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret

def gatherData(name):
    prPurple("Matrix " + name)
    try:
        numRow = int(input(makeCyan("Enter the number of rows: ")))
        numCol = int(input(makeCyan("Enter the number of columns: ")))
        if numRow != numCol:
            prRed("Matrix Is Not Square")
            exit()
    except:
        prRed("That is not a number")
        exit()
    try:
        entries = list(map(float , input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = reshape_list(entries,numRow)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prPurple(name + "=")
    for i in range(0,len(matrix)):
        prLightGray(matrix[i])
    prYellow("------------")
    return matrix

def reshape_list(L, xsize, ysize=None, fillna=False):
    gap = []
    v, r = divmod(len(L),xsize)
    gap = [None]*r
    return list(map(list, zip(*[iter(L+gap)]*xsize)))

if __name__ == "__main__":
    main()
