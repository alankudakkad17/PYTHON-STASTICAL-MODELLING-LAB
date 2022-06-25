import matplotlib.pyplot as plt
x=[1,8,1,8,1,8]#assign an array
plt.plot(x)#to plot the array
plt.xlabel("x-axis")
plt.ylabel('y-axis')
plt.grid()
plt.show()
plt.figure()#to insert a new figure
plt.stem(x)#to visualize stem plot of same array x
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.show()
