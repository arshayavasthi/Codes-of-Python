from matplotlib import pyplot as plt
import numpy as np
x,y=np.loadtxt('tec.csv',unpack=True,delimiter = ',')
plt.scatter(x,y)
plt.show()
