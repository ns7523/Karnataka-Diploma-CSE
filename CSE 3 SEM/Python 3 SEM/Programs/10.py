print("***Built-in functions***")
n=int(input("enter integer number"))
print("binary value of",n,"is:",bin(n))
print("octal value of",n,"is:",oct(n))
print("hexa value of",n,"is:",hex(n))
print("the square of",n,"is:",pow(n,2))
print("the cube of",n,"is:",pow(n,3))
print("total number of built-in functions in python=",len(dir(__builtins__)))
print("list of all built-in functions in python")
print(dir(__builtins__))


