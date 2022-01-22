import numpy as np
import matplotlib.pyplot as plt
import math

def modified_euler_method(f, a, b, N, condition):
	h = (b - a)/N
	t = np.arange(start = a, stop = b, step = h)
	w = condition
	print("%6.1f \t\t %f" % (t[0],w))
	for i in range(N-1):
		w = w + (h/2)*(f(t[i],w) + f(t[i+1], w + h*f(t[i], w)))
		print("%6.1f \t\t %f" % (t[i],w))

def f(t, y):
	return y - t**2 + 1
	
modified_euler_method(f, 0, 2, 10, 0.5)