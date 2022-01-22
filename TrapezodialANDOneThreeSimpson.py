import numpy as np
import matplotlib.pyplot as plt

def trapezodial(intervals, exactValue, x0, xN):
	interval_values = np.zeros(len(intervals))
	error = np.zeros(len(intervals))
	for j, n in enumerate(intervals):
		h = (xN - x0) / n
		x = np.arange(start = x0, stop = xN + h, step = h)
		k = len(x) - 1
		interval_values[j] = f(x[0]) / 2
		for i in range(1, k, 1):
			interval_values[j] += f(x[i])
		interval_values[j] = h * (interval_values[j] + f(x[k])/2)
		error[j] = np.abs(exactValue - interval_values[j])
	return error

def one_three_Simpson(intervals, exactValue, x0, xN):
	interval_values = np.zeros(len(intervals))
	error = np.zeros(len(intervals))
	for j, n in enumerate(intervals):
		h = (xN - x0) / n
		x = np.arange(start = x0, stop = xN + h, step = h)
		k = len(x) - 1
		interval_values[j] = f(x[0])
		for i in range(1, k, 1):
			if i % 2 != 0:
				interval_values[j] += 4 * f(x[i])
			else:
				interval_values[j] += 2 * f(x[i])
		interval_values[j] = (h/3) * (interval_values[j] + f(x[k]))
		error[j] = np.abs(exactValue - interval_values[j])
	return error
	
f = lambda x: np.exp(-np.power(x, 2))
error_trapezodial = trapezodial(intervals = [10, 20, 40, 80, 160], exactValue = 0.74682413279, x0 = 0, xN = 1)
error_one_three_Simpson = one_three_Simpson(intervals = [2, 4, 8, 16, 32], exactValue = 0.74682413279, x0 = 0, xN = 1)

print('Errors Trapezodial: {} \nErrors 1/3 Simpson: {}'.format(error_trapezodial, error_one_three_Simpson))

fig, ax = plt.subplots(2, figsize = (10,14))
ax[0].set(xlabel = '# intervals', ylabel = 'Error', title = 'Trapezodial Method')
ax[1].set(xlabel = '# intervals', ylabel = 'Error', title = '1/3 Simpson')
ax[0].grid()
ax[1].grid()
ax[0].plot([10, 20, 40, 80, 160], error_trapezodial, 'go-')
ax[1].plot([2, 4, 8, 16, 32], error_one_three_Simpson, 'bo-')
plt.show()