import numpy as np
import matplotlib.pyplot as plt

yV1 = [ 1.000000, 0.731689, 0.070737, -0.628174, -0.989992, -0.820559, -0.210796, 0.512085, 0.960170 ]
yV2 = [ 0.00000, 0.68164, 0.99749, 0.77807, 0.14112, -0.57156, -0.97753, -0.85893, -0.27942  ]

xVec = np.linspace(0, 2, len(yV1))

minIm = min(min(yV1), min(yV2))
maxIm = max(max(yV1), max(yV2))

fig, ax = plt.subplots(figsize = (10,7))

ax.set_xlim(left=0, right=2)
ax.set_ylim(bottom=minIm, top=maxIm)

counterIn, counterOut = 0, 0
n = 2000

np.random.seed(0)
for _ in range(n):
	x = 2 * np.random.random()
	y = minIm + (maxIm - minIm) * np.random.random()
	
	j = 1
	while xVec[j] < x:
		j = j + 1
		
	#Splines
	y1 = yV1[j-1] + ((yV1[j] - yV1[j-1]) / (xVec[j] - xVec[j-1])) * (x - xVec[j-1])
	y2 = yV2[j-1] + ((yV2[j] - yV2[j-1]) / (xVec[j] - xVec[j-1])) * (x - xVec[j-1])

	minD = min(y1, y2)
	minU = max(y1, y2)

	if minD < y and y < minU:
		plt.plot(x, y, 'b+')
		counterIn = counterIn + 1
	else:
		plt.plot(x, y, 'y*')
		counterOut = counterOut + 1
		
#Monte Carlo
integral = (max(xVec) - min(xVec)) * (maxIm - minIm) * (counterIn / n)
ax.set_title('Integral: {}'.format(integral))
plt.show()