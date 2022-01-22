import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix

n = 1000
A = np.zeros(n)
for i in range(n):
	for j in range(n):
		if i==j:
			A[i][j] = 2.0
		elif j == i+1:
			A[i][j] = -1.0
		elif i == j+1:
			A[i][j] = -1.0
			
B = np.zeros(n)
for i in range(n-1):
	B[i][i] = 2.0
	B[i][i+1] = -1
	B[i+1][i] = -1
B[n, n] = 2
print(B)

C = np.diag(2 * np.ones(n,1)) + np.diag(-np.ones(n-1, 1), 1) + np.diag(-np.ones(n-1, 1), -1)
print(C)

S = csr_matrix(A)
print(S)