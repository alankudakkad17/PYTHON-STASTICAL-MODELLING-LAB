def volArea(r,h):
    vol=(3.14*r*r*h)
    sa=(2*3.14*r*h)
    tsa=((2*3.14*r*h)+(3.14*r*r*2))
    print("Volume of the cylinder =",vol)
    print("Curved Surface Area of the cylinder =",sa)
    print("Total Surface Area of the cylinder =",tsa)
r=float(input("Enter the radius of cylinder : "))
h=float(input("Enter the height of cylinder : "))
volArea(r,h)
