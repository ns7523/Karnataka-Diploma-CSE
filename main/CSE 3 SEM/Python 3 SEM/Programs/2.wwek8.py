def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    print("AT OPT")
    print("1.addition \t 2.subtraction \t 3.multiplication \t 4.division ")
    choice=int(input("ENTER A CHOICE : "))
    x=int(input("ENTER value for x :"))
    y=int(input("ENTER value for y:"))
    if choice==1:
        print("addition :",add(x,y))
    elif choice==2:
        print("subtraction :",sub(x,y))
    elif choice==3:
        print("multiplication :",multi(x,y))
    elif choice==4:
        print("division :",div(x,y))
    else:
        print("Invalid choice")
