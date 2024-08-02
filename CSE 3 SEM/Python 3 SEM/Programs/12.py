print("***factorial***")
def fact(n):
 if n==1:
  return n
 else:
  return n*fact(n-1)
n=int(input("enter positive number"))
if n==0:
 print("factorial of 0 is 1")
elif n<0:
 print("invalid input")
else:
 ans=fact(n)
 print("factorial of",n,"is:",ans)
