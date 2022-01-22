import numpy as np
import matplotlib.pyplot as plt
from RectangleRule import rectangle_rule

def romberg_integration(f, a, b, eps, nmax):
	Q = np.zeros((nmax, nmax), float)
	converged = 0
	for i in range(nmax):
		N = 2**i
		Q[i, 0] = rectangle_rule(f, a, b, N)
		for k in range(i):
			n = k + 2
			Q[i, k+1] = 1.0/(4**(n-1)-1)*(4**(n-1)*Q[i,k] - Q[i-1,k])
		if i>0:
			if (abs(Q[i,k+1] - Q[i,k]) < eps):
				converged = 1
				break
	print (Q[i, k+1], N, converged)
	return (Q[i, k+1], N, converged)
	
def romberg(f, a, b, p):
	I = np.zeros((p, p))
	for k in range(p):
		I[k, 0] = rectangle_rule(f, a, b, 2**k)
		for j in range(k):
			I[k, j+1] = (4**(j+1) * I[k,j] - I[k-1,j])/(4**(j+1) - 1)
		#print(I[k,0:k+1])
	print (I[k, j+1])
	return I
	
f = lambda x: np.power(x, 2)-2*x+3
print(romberg_integration(f, -5, 10, 1.0e-10, 10))
romberg(f, -5, 10, 10)
