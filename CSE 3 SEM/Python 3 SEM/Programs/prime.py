start=int(input("Enter starting number :"))
end=int(input("Enter ending number :"))
for n in range(start,end):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            print("PRIME NUMBER",n)
