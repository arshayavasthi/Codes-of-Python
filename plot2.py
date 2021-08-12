from matplotlib import pyplot as plt
x=[1,2,3,4,5,6]
y=[2,3,4,5,6,7]
plt.plot(x,y,color='green',linestyle='dotted',linewidth=13,marker='o',markerfacecolor='blue',markersize=22)
x1=[1,21,3,34,5,6]
y2=[22,3,14,5,46,7]
plt.plot(x1,y2,color='red',linestyle='dotted',linewidth=11,marker='s',markerfacecolor='black',markersize=12)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title("my first graph")
plt.show()
