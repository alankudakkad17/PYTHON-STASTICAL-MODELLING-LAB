import random
E=0
l=[]
q=[]
n=int(input(" No. of times 2 Die are tossed : "))
for i in range(1,n+1):
    s1=random.randint(1,6)
    l.append(s1)
    s2=random.randint(1,6)
    q.append(s2)
    if(s1+s2==8):
        E=E+1
print(l,q)
print("probability of 8 in 2 Die toss : ",float(E/n))
