name=input("NAME :")
regno=input("REGNO :")
branch=input("BRANCH :")
sem=input("SEM :")
py=int(input("ENTER PYTHON MARKS :"))
ch=int(input("ENTER CH MARKS :"))
cn=int(input("ENTER CN MARKS :"))
dbms=int(input("ENTER DBMS MARKS :"))
if py<0 or py>100 or ch<0 or ch>100 or cn<0 or cn>100 or dbms<0 or dbms>100:
    print("ENTER VALID MARKS ")
else:
    print(name)
    print(regno)
    print(branch)
    print(sem)
    print("PYTHON MARKS :",py)
    print("CH MARKS :",ch)
    print("CN MARKS :",cn)
    print("DBMS MARKS:",dbms)
    total=py+ch+cn+dbms
    average=total/4
    print("TOTAL MARKS :",total)
    print("AVERAGE MARKS :",average)
    if py<35 or ch<35 or cn<35 or dbms<35:
        print("FAIL")
    elif average>85:
        print(" A + ")
    elif average>=70 and average<85:
        print("B ")
    elif average>=60 and average<70:
        print("C")
    else:
        print("D")
    
