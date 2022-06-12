file =open('h1','r')
f=0
E=[]
for x in file:
    e=x.split(" ")
e.remove('\n')
for x in e:
    z=int(x)
    v=int(z+1/2)
    for y in range(2,v):
        if(z%y==0):
            f=1
            break
    if(f==0):
        E.append(z)  
    f=0
print("prime numbers:",E)
