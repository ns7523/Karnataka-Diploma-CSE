import math as m
print("*** Built-in math module***")
a=int(input("Enter a number to obtain square root :"))
print("Square-root of a : ",m.sqrt(a))
print("PI value is :",m.pi)
b=int(input("Trignometry ---- Enter value :"))
print("cos ",b,"is :",m.cos(b))
print("sin ",b,"is :",m.sin(b))
print("tan ",b,"is :",m.tan(b))
c=int(input("Factorial ---- Enter value : "))
print("factorial of ",c,"is :",m.factorial(c))
print("-----List of functions , variables , classes in Math module-----")
print(dir(m))
import random as r
print("*** built-in Random module ***")
print(r.random())
print(r.random()*100)
l1=[1,4,800,"Python",27,"Hello"]
print(r.choice(l1))
print("-----List of functions,variables,classes----- ")
print(dir(r))




