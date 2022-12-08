from Printing import *

def main():
    A = gatherData()
    prPurple("The Reduced Row Echelon Form Is:")
    print_matrix(rref(A))

def rref(matrix):
  # Make a copy of the matrix so we don't modify the original
  rref_matrix = matrix.copy()

  # Get the number of rows and columns of the matrix
  rows = len(rref_matrix)
  cols = len(rref_matrix[0])

  # Keep track of the current row and column we are working on
  current_row = 0
  current_col = 0

  # Loop through the rows and columns of the matrix
  while current_row < rows and current_col < cols:
    # Find the first non-zero element in the current column
    non_zero_row = None
    for row in range(current_row, rows):
      if rref_matrix[row][current_col] != 0:
        non_zero_row = row
        break

    # If we didn't find a non-zero element, move on to the next column
    if non_zero_row is None:
      current_col += 1
      continue

    # Swap the current row and the row with the non-zero element
    rref_matrix[current_row], rref_matrix[non_zero_row] = rref_matrix[non_zero_row], rref_matrix[current_row]

    # Divide the current row by the leading coefficient
    leading_coeff = rref_matrix[current_row][current_col]
    rref_matrix[current_row] = [value / leading_coeff for value in rref_matrix[current_row]]

    # Eliminate the leading coefficient in the other rows
    for row in range(rows):
      if row == current_row:
        continue

      leading_coeff = rref_matrix[row][current_col]
      rref_matrix[row] = [rref_matrix[row][col] - leading_coeff * rref_matrix[current_row][col] for col in range(cols)]

    # Move on to the next row and column
    current_row += 1
    current_col += 1

  # Return the reduced row echelon form of the matrix
  return rref_matrix

def gatherData():
    prPurple("Set values of matrix:")
    try:
        numRow = int(input(makeCyan("Enter the number of rows: ")))
        numCol = int(input(makeCyan("Enter the number of columns: ")))
    except:
        prRed("That is not a number")
        exit()
    try:
        entries = list(map(float , input(makeCyan("Entries (seperated by a space): ")).split()))
        matrix = reshape_list(entries,numCol)
    except:
        prRed("Matrix is not properly formatted")
        exit()
    prPurple("Matrix=")
    print_matrix(matrix)
    return matrix

def reshape_list(L, xsize, ysize=None, fillna=False):
    gap = []
    v, r = divmod(len(L),xsize)
    gap = [None]*r
    return list(map(list, zip(*[iter(L+gap)]*xsize)))

def print_matrix(matrix):
    for i in range(0,len(matrix)):
        prLightGray(matrix[i])

if __name__ == "__main__":
    main()
