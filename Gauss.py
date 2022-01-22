import numpy as np
import matplotlib.pyplot as plt

def lowerTriangularSolver(A, b):
	if b.shape[1] != 1:
		return 'b must be a column vector 2D dimension with shape = (something, 1)'
	elif A.shape != (b.shape[0], b.shape[0]):
		return '{} is not equal to ({}, {})'.format(A.shape, b.shape[0], b.shape[0])
		
	x = np.zeros(b.shape)
	for i in range(b.shape[0]):
		for j in range(i):
			b[i] = b[i] - A[i, j] * x[j]
		x[i] = b[i] / A[i, i]
	
	return x
	
def upperTriangularSolver(A, b):
	y = lowerTriangularSolver(np.transpose(A), np.transpose(b))
	return np.transpose(y)
	
A = np.array([[1, 0, 0], [-1, 1, 0], [1, 1, 1]])
print('A = \n{}'.format(A))

b = np.array([[1], [2], [3]])
print('\nb = \n{}'.format(b))

print('\nx = \n{}'.format(lowerTriangularSolver(A, b)))
print('=========================================================')

A = np.array([[1, 1, 1], [0, -1, 1], [0, 0, 1]])
print('A = \n{}'.format(A))

b = np.array([[1, 2, 3]])
print('\nb = \n{}'.format(b))
print('\nx = \n{}'.format(upperTriangularSolver(A, b)))