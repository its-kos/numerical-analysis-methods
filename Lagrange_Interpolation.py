import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x, y, z):
	val = np.zeros(z.shape)
	for k in range(z.shape[0]):
		for i, x_i in enumerate(x):
			p = 1
			for j, x_j in enumerate(x):
				if i != j:
					p = p * (z[k] - x[j]) / (x[i] - x[j])
			val[k] = val[k] + p * y[i]
	return val
	
f = lambda x: 1/(1 + 25 * np.power(x, 2))
z = np.linspace(-1, 1, num=39)
true_values = f(z)

#Uniform Partioning
x1 = np.linspace(-1, 1, num=20)
y1 = f(x1)
uniformInteger = lagrange_interpolation(x1, y1, z)

#Chebyshev
i = np.arange(1, 21)
x2 = np.cos(((2 * i - 1) * np.pi) / (2 * len(i)))
y2 = f(x2)
chebyshevInteger = lagrange_interpolation(x2, y2, z)

fig, ax = plt.subplots(figsize = (10,8))
ax.plot(z, true_values, 'ko-', label = 'True Values')
ax.plot(z, uniformInteger, 'g*-', label = 'Uniform Interpolation')
ax.plot(z, chebyshevInteger, 'y--', label = 'Chebyshev Interpolation')
ax.grid()
ax.legend()
plt.show()