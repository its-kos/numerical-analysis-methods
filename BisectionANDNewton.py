import numpy as np
import matplotlib.pyplot as plt

def bisection():
	x1 = 0
	x2 = 2
	iterations = 0
	
	errorBisection = [np.abs(x2 - x1)]
	
	while errorBisection[iterations] > 0.0001:
		iterations = iterations + 1
		b = (x2 - x1) / 2
		if f(b) == 0:
			errorBisection[iterations] = 0
			print('{} Iterations, x* = {}, f(x*) = {}'.format(iterations + 1, b, f(b)))
			break
		elif f(x1)*f(b) < 0:
			x2 = b
		else:
			x1 = b
			
		errorBisection.append(np.abs(x2 - x1))
	print('BISECTION: {} Iterations , x* = {} , f(x*) = {}'.format(iterations + 1, b, f(b)))
	return errorBisection
	
def newton():
	x1 = 2
	x2 = x1 - f(x1) / df(x1)
	iterations = 0
	
	errorNewton = [np.abs(x2 - x1)]
	while errorNewton[iterations] > 0.0001:
		iterations = iterations + 1
		x1 = x2
		x2 = x1 - f(x1) / df(x1)
		errorNewton.append(np.abs(x2 - x1))
	print('NEWTON: {} Iterations, x* = {}, f(x*) = {}'.format(iterations, x2, f(x2)))
	return errorNewton
	
f = lambda x: np.exp(x) - 2
df = lambda x: np.exp(x)

x = np.arange(0, 2, 0.1)
y = f(x)
fig, ax = plt.subplots(2, figsize=(13, 16))

ax[0].plot(x, y, label = 'e^x - 2')
ax[0].set_xlim(left=-1, right=2)
ax[0].set_ylim(bottom=-1, top=6)
ax[0].grid()
ax[0].legend()

errorNewton, errorBisection = newton(), bisection()

ax[1].plot(np.arange(len(errorNewton)), errorNewton, 'k*-', label = 'Newton Error')
ax[1].plot(np.arange(len(errorBisection)), errorBisection, 'yo-', label = 'Bisection Error')
ax[1].set(xlabel='Iterations', ylabel='Error')
ax[1].grid()
ax[1].legend()