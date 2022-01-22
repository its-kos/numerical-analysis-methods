import numpy as np
import matplotlib.pyplot as plt
import math

def runge_kutta_order_four(f, a, b, N, condition):
	h = (b - a)/N
	t = a
	w = condition
	print("%6.1f \t\t %f" % (t,w))
	for i in range(1, N):
		K1 = h * f(t, w)
		K2 = h * f(t + h/2, w + K1/2)
		K3 = h * f(t + h/2, w + K2/2)
		K4 = h * f(t + h, w + K3)
		w = w + (K1 + 2*K2 + 2*K3 + K4)/6
		t = a + i*h
		print("%6.1f \t\t %f" % (t,w))
	
def f(t, y):
	return y - t**2 + 1
	
runge_kutta_order_four(f, 0, 2, 10, 0.5)