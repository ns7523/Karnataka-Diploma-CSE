print("*** Area ***")
cir=lambda r:3.14*r*r
sq=lambda s:s*s
rec=lambda h,w:h*w
r=int(input("Enter radius of Circle :  "))
print("The Area of circle = ",cir(r))
s=int(input("Enter side of Square :  "))
print("The Area of Square = ",sq(s))
h=int(input("Enter height of rectangle : "))
w=int(input("Enter width of rectangle : "))
print("The Area of rectangle = ",rec(h,w))
