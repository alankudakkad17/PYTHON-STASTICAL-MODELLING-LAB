import random
import matplotlib.pyplot as plt
import numpy as np
n=int(input("Enter the no.of tosses:"))
h=t=y=0
z=[]
for i in range(n+1):
            flip = random.randint(0, 1)
            if(flip==0):
                t=t+1
                y=h/n
                z.append(y)
            elif(flip==1):
                h=h+1
                y=h/n
                z.append(y)
print(z)
print("probability of heads=",(h/n))
q=[]
for x in range(0,n+1):
    q.append(x)
print(q)
plt.plot(z,q)
plt.show()
