from matplotlib import pyplot as plt
x1=[1,2,3]
y1=[2,4,1]
plt.plot(x1,y1,label="label 1")
x2=[1,2,3]
y2=[4,1,3]
plt.plot(x2,y2,label="label 2")
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("my plot")
plt.legend()
plt.show()

