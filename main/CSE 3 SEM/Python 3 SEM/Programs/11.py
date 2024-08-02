print("***simple calculator***")
def add(x,y):
 return x+y
def sub(x,y):
 return x-y
def mul(x,y):
 return x*y
def div(x,y):
 return x/y
while True:
 print("1.addition \t 2.subtraction \t 3.multiplication \t 4.division")
 choice=int(input("enter your choice"))
 x=int(input("enter 1st integer number"))
 y=int(input("enter 2nd integer number"))
 if choice is 1:
  print("the addition of 2 numbers is:",add (x,y))
 elif choice is 2:
  print("the subtraction of 2 numbers is:",sub (x,y))
 elif choice is 3:
  print("the multiplication of 2 numbers is:",(x,y))
 elif choice is 4:
  print("the division of 2 numbers is:",div(x,y))
 else:
  break
