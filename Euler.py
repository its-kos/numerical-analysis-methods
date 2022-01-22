import numpy as np
import matplotlib.pyplot as plt

def simple_euler(f, y0, a, b, h):
	t, y = a, y0
	while t <= b:
		print("%6.3f %6.3f" % (t,y))
		t += h
		y += h * f(t, y)

def f(y, t):
	return (y/t) - (y/t)**2
	
simple_euler(f, 1, 0, 100, 5)