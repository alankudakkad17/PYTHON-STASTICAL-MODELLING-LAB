F=[60,54,46,41]
Ftot =201
M=[40,44,53,57]
Mtot=199
Tot=[100,98,99,98]
Fx=[]
Mx=[]
val=0
for i in Tot:
    val=i*(201/395)
    Fx.append(val)
print("Expected Female ",Fx)
valm=0
for i in Tot:
    valm=(i*194/395)
    Mx.append(valm)
print("Expected Male ",Mx)
u=v=0
for i in range(0,4):
    u=u+((F[i]-Fx[i])**2)/Fx[i]
    v=v+((M[i]-Mx[i])**2)/Mx[i]

print("Female chisquare=",u)
print("Male Chisquare=",v)  
print("Mean Chi Square =",(u+v))
