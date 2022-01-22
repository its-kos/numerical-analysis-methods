import numpy as np
import matplotlib.pyplot as plt

#Implicit Trapezodial Rule
def trap(f, a, b, n, error):
	h = (b - a) / n
	x = np.arange(start = a, stop = b + h, step = h)
	k = len(x) - 1
	interval_values = f(a) / 2
	for i in range(1, k, 1):
		interval_values += f(x[i])
	interval_values = h * (interval_values + f(x[k])/2)
	return interval_values
	
f = lambda x: (np.power(x, 2))*np.sin(x)
print(trap(f, 0, np.pi, 25, 0.0001))


	