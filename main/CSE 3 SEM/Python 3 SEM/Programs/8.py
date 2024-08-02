print("***dictionary indexing***")
sub={1:"python",2:"ch",3:"cn",4:"dbms"}
print("the 1 sub is:",sub[1])
print("the 2 sub is:",sub[2])
print("the 3 sub is:",sub[3])
print("the 4 sub is:",sub[4])
print("\n***dictionary iterating ***")
for k in sub:
 print("the key is:",k,"the value is:",sub[k])
print("\n***dictionary comprehension***")
comp={i : i**3 for i in range(1,11)}
print(comp)
