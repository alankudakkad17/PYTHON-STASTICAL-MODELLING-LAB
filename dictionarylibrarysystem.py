d1 ={"b1": 5,"b2": 3,"b3": 4}
print("\n1:add stock\n2:delete stock\n3:to add new book\n4:exit")
n=int(input("Enter your choice:"))
while(n!=4):
    if(n==1):
        print(d1)
        z=input("enter the  book name:")
        y=int(input("enter the no.of stocks you are adding:"))
        d1[z]=d1[z]+y
    elif(n==2):
        print(d1)
        z=input("enter the book name:")
        y=int(input("enter the no.of stocks you are deleting:"))
        d1[z]=d1[z]-y
    else:
        print(d1)
        z=input("enter the book name:")
        u=int(input("enter the no.of stocks:"))
        d1.update({z:u})
    print("\n1:add stock\n2:delete stock\n3:to add new book\n4:exit")
    n=int(input("Enter your choice:"))
print(d1)
