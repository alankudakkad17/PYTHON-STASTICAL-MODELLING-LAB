import matplotlib.pyplot as plt
plt.figure()
e=[]
for x in range(0,11):
    y=x**4+5
    e.append(y)
plt.plot(e)
plt.xlabel("x-axis",color='green')
plt.ylabel('y-axis',color='green')
plt.grid()
plt.show()
plt.show()
