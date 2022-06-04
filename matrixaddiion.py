R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
m1 = []
print("Enter the entries rowwise:")
for i in range(R):
    a =[]
    for j in range(C):
         a.append(int(input()))
    m1.append(a)
m2=[]
print("Enter the second matrix:")
for i in range(R):  
    b =[]
    for j in range(C):  
         b.append(int(input()))
    m2.append(b)
print("resultant matrix:")
S=[]                                   #
for i in range(R):                     #
    s=[]                               #
    for j in range(C):                 # FUNCTION TO ADD THE MATRICES
        sum=m1[i][j]+m2[i][j]            #
        s.append(sum)                  #
    S.append(s)
for i in range (R):                 #
    for j in range (C):             # FUNCTION TO PRINT THE MATRIX
        print(S[i][j],end=" ")    #
    print()  
