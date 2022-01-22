import numpy as np
import matplotlib.pyplot as plt

class Data:
	def __init__(self, x, y):
		self.x = x
		self.y = y


def lagrange_interpolation(f, x_i, n):
	result = 0
	for i in range(n):
		term = f[i].y
		for j in range(n):
			if j != i:
				term = term * (x_i - f[j].x) / (f[i].x - f[j].x)
		result += term
	return result
	
f = [0., 0., 0., 0.]
f[0] = Data(0, 2)
f[1] = Data(1, 3)
f[2] = Data(2, 12)
f[3] = Data(5, 147)
print(lagrange_interpolation(f, 3, 4))