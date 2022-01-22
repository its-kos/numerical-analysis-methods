import numpy as np
import matplotlib.pyplot as plt

def rectangle_rule(f, a, b, N):
	cumulative_area = 0
	a = float(a)
	b = float(b)
	N = float(N)
	h = (b - a)/N
	trailing_x = a
	leading_x = a + h
	while(a <= leading_x <= b) or (a >= leading_x >= b):
		area = f((trailing_x + leading_x)/2) * h
		cumulative_area += area
		leading_x += h
		trailing_x += h
	return cumulative_area