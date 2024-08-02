print("Annonymous Functions")
circle=lambda r:3.14*r*r
triangle=lambda h,b:0.5*h*b
square=lambda s:s*s
rectangle=lambda l,w:l*w
r=int(input("Enter radius : "))
print("Area of circle : ",circle(r))
h=int(input("Enter height for traingle :"))
b=int(input("Enter base for traingle :"))
print("Area of triangle :",triangle(h,b))
s=int(input("Enter side of square :"))
print("Area of square :",square(s))
l=int(input("Enter length for rectangle :"))
w=int(input("Enter width for rectangle :"))
print("Area of rectangle :",rectangle(l,w))
