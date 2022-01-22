import numpy as np
import matplotlib.pyplot as plt

"""def richardson(f, x, n, h):
	D = np.array([[0] * (n + 1)] * (n + 1), float)
	for i in range(n+1):
		D[i,0] = 0.5 * (f(x+h) - f(x-h))/h
		powerOf4 = 1
		for j in range(1, i+1):
			D[i, j] = D[i, j] + (D[i, j-1] - D[i-1, j-1]) / (powerOf4 - 1)
		h = 0.5 * h
	return D
	
f = lambda x: np.power(x, 4)
print(richardson(f, 3, 5, 0.25))"""

f = -y^2
y0 = 1