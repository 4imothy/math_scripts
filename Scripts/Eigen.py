from Printing import *
import numpy as np

def main():
    a = gatherData()
    try:
        val, vec = np.linalg.eig(a)
    except:
        prRed("Computation did not converge")
        exit()
    prPurple("The EigenValues Are: ")
    prLightGray(', '.join(map(str, val)))
    prPurple("The EigenVectors Are: ")
    for i in range(0,len(vec[0])):
        prLightGray(str(vec[:,i]) + ",")

def gatherData():
    prPurple("Enter Matrix")
    try:
        numRow = int(input(makeCyan("Enter the number of rows: ")))
        numCol = int(input(makeCyan("Enter the number of columns: ")))
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
    prYellow("------------")
    return matrix

if __name__ == "__main__":
    main()
