a=(10,5,4,3,2)
print("The tuple is",a)
ev=[]
odd=[]
for i in a:
    if(i%2==0):
        ev.append(i)   
    else:
        odd.append(i)
print("The even tuple are:")
print(tuple(ev))
print("The odd tuple are:")  
print(tuple(odd))
