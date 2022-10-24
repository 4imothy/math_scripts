import numpy as np

def strassen(X, Y):
  if len(X) == 1:
    return [[X[0][0] * Y[0][0]]]
  else:
    A, B, C, D = divide_matrix(X)
    E, F, G, H = divide_matrix(Y)

    P1 = strassen(A, sub_matrix(F,H))
    P2 = strassen(add_matrix(A, B), H)
    P3 = strassen(add_matrix(C, D), E)
    P4 = strassen(D, sub_matrix(G, E))
    P5 = strassen(add_matrix(A, D), add_matrix(E, H))
    P6 = strassen(sub_matrix(B, D), add_matrix(G, H))
    P7 = strassen(sub_matrix(A, C), add_matrix(E, F))

    Z11 = add_matrix(sub_matrix(add_matrix(P5, P4), P2), P6)
    Z12 = add_matrix(P1, P2)
    Z21 = add_matrix(P3, P4)
    Z22 = sub_matrix(sub_matrix(add_matrix(P5, P1), P3), P7)


    return np.matrix(merge_matrix(Z11, Z12, Z21, Z22))

def sub_matrix(X, Y):
  n = len(X)
  if n == 1:
    return [[X[0][0] - Y[0][0]]]
  S = []
  for i in range(n):
    S.append([])
    for j in range(n):
      S[i].append(X[i][j] - Y[i][j])
  return S

def add_matrix(X, Y):
  n = len(X)
  if n == 1:
    return [[X[0][0] + Y[0][0]]]
  S = []
  for i in range(n):
    S.append([])
    for j in range(n):
      S[i].append(X[i][j] + Y[i][j])
  return S

def merge_matrix(matrix_11, matrix_12, matrix_21, matrix_22):
  matrix_total = []
  rows1 = len(matrix_11)
  rows2 = len(matrix_21)
  for i in range(rows1):
    matrix_total.append(matrix_11[i] + matrix_12[i])
  for j in range(rows2):
    matrix_total.append(matrix_21[j] + matrix_22[j])
  return matrix_total

def divide_matrix(A):
  mid = len(A)//2
  m_11 = [M[:mid] for M in A[:mid]]
  m_12 = [M[mid:] for M in A[:mid]]
  m_21 = [M[:mid] for M in A[mid:]]
  m_22 = [M[mid:] for M in A[mid:]]

  return (m_11, m_12, m_21, m_22)
