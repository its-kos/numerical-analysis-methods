import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

def exponentTaylor(n, x):
	y = np.zeros(x.shape)
	for i, x_i in enumerate(x):
		s, term = 1, 1
		for k in range(1, n+1):
			term = (term * x_i) / k
			s += term
		y[i] = s
	return y
	
x = np.arange(start = -0.5, stop = 1.5, step = 0.1)
fig, ax = plt.subplots(figsize=(10,8))

ax.plot(x, np.exp(x), 'k', label = 'exp')
ax.plot(x, exponentTaylor(0, x), 'g', label = 'zero order')
ax.plot(x, exponentTaylor(1, x), 'b', label = 'first order')
ax.plot(x, exponentTaylor(2, x), 'r', label = 'second order')

ax.grid()
ax.legend()
plt.show()