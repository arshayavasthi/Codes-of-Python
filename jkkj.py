from matplotlib import pyplot as plt
ages=[10,20,30,40,66]
range=(0,100)
bins=2
plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.2)
plt.show()
