import numpy as np
import matplotlib.pyplot as plt
import math

def Cholesky_Decomposition(A, n):
	L = np.zeros((n+1, n+1))
	for i in range(n):
		for j in range(i + 1):
			sum1 = 0
			if (j == i):
				for k in range(j):
					sum1 += pow(L[j][k], 2)
				L[j][j] = int(math.sqrt(A[j][j] - sum1))
			else:
				for k in range(j):
					sum1 += (L[i][k] * L[j][k])
				if(L[j][j] > 0):
					L[i][j] = int((A[i][j] - sum1) / L[j][j])
	print("Lower Triangular\t\tTranspose")
	for i in range(n):
		for j in range(n):
			print(L[i][j], end = "\t")
		print("", end = "\t")
		for j in range(n):
			print(L[j][i], end = "\t")
		print("")
		
n = 3
A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
Cholesky_Decomposition(A, n)