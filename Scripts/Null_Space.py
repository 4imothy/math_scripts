from scipy.linalg import null_space
from Printing import *
import numpy as np

def main():
    m = gatherData("Matrix")
    prPurple("Nullspace=")
    prLightGray(null_space(m))

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
        matrix = reshape_list(entries,numRow)
    except:
        prRed(name + " is not properly formatted")
        exit()
    prPurple(name + "=")
    prLightGray(matrix)
    prYellow("------------")
    return matrix

def reshape_list(L, xsize, ysize=None, fillna=False):
    gap = []
    v, r = divmod(len(L),xsize)
    gap = [None]*r
    return list(map(list, zip(*[iter(L+gap)]*xsize)))

if __name__ == "__main__":
    main()
