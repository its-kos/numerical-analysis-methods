import numpy as np
import matplotlib.pyplot as plt

def three_eights_Simpson(f, a, b, exactValue, intervals):
	a = float(a)
	b = float(b)
	interval_values = np.zeros(len(intervals))
	error = np.zeros(len(intervals))
	for j, n in enumerate(intervals):
		h = (b - a)/n
		x = np.arange(start = a, stop = b + h, step = h)
		k = len(x) - 1
		interval_values[j] = f(x[0])
		for i in range(1, k, 1):
			if i%3 == 0:
				interval_values[j] += 2 * f(x[i])
			else:
				interval_values[j] += 3 * f(x[i])
		interval_values[j] = ((3*h)/8) * (interval_values[j] + f(x[k]))
		error[j] = np.abs(exactValue - interval_values[j])
	return interval_values, error
	
f = lambda x: np.power(x, 4)
approx, error = three_eights_Simpson(f, 0, 5, 625, intervals = [1000, 2000, 3000, 4000, 5000])
print(approx, error)
print('Errors 3/8 Simpson: {}'.format(error))
fig, ax = plt.subplots(figsize = (10, 15))
ax.set(xlabel = '# intervals', ylabel = 'Error', title = '3/8 Simpson')
ax.grid()
ax.plot([1000, 2000, 3000, 4000, 5000], error, 'bo-')
plt.show()