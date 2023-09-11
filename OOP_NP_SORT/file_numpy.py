import numpy as np
x1 = np.genfromtxt('wine.data',delimiter=',', usecols=[1])
y1 = np.genfromtxt('wine.data', delimiter=',', usecols=[2])
x2 = np.genfromtxt('wine.data',delimiter=',', usecols=[1])
y2 = np.genfromtxt('wine.data', delimiter=',', usecols=[3])

from matplotlib import pyplot as plt
plt.scatter(x1,y1, color="#FF7F50", marker="x")
plt.scatter(x2,y2, color="#6495ED", marker="v")
# plt.scatter(x,y)
plt.show()