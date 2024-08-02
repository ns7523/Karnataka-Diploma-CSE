print("*** Dictionary Indexing ***")
sub={1:"Python",2:"CH",3:"CN",4:"DBMS"}
print("The 1 Sub is : ",sub[1])
print("The 2 Sub is : ",sub[2])
print("The 3 Sub is : ",sub[3])
print("The 4 Sub is : ",sub[4])
print("*** Dictionary Iteration ***")
for k in sub:
    print("The key is :",k,",The value is :",sub[k])
print("*** Dictionary Comprehension ***")
comp={i:i**3 for i in range(1,11)}
print(comp)
