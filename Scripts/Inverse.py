from Printing import *
import numpy as np

def main():
    M = gatherData("Matrix")
    # create identity matrix to operate on
    Inv = invert_matrix(M, np.identity(M.shape[1]))
    prPurple("Inverse Matrix=")
    prLightGray(Inv)

def invert_matrix(AM, IM):
    for fd in range(len(AM)):
        fdScaler = 1.0 / AM[fd][fd]
        for j in range(len(AM)):
            AM[fd][j] *= fdScaler
            IM[fd][j] *= fdScaler
        for i in list(range(len(AM)))[0:fd] + list(range(len(AM)))[fd+1:]:
            crScaler = AM[i][fd]
            for j in range(len(AM)):
                AM[i][j] = AM[i][j] - crScaler * AM[fd][j]
                IM[i][j] = IM[i][j] - crScaler * IM[fd][j]
    return IM

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
        entries = list(map(np.double, input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = np.array(entries).reshape(numRow, numCol)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prPurple(name + "=")
    prLightGray(matrix)
    prYellow("------------")
    return matrix

if __name__ == "__main__":
    main()
