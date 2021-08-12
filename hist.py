from matplotlib import pyplot as plt
ages=[2,3,4,5,23,34,45,2,12,23,2,3,3,4,3,4,3,4,3,4,3,4,2,23,2,3,2,3,23,12,23,34,56,89,90]
range=(0,100)
bins=10
plt.hist(ages,bins,range,color='red',histtype='bar',rwidth=0.2)
plt.show()
