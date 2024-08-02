print("*** Dictionary operations *** ")
std={"name":"NS.Akash","regno":"498CS21047","branch":"CSE"}
print("The Student dictionary is : ",std)
print("The student name is : ",std["name"])
print("The student RegNo is : ",std["regno"])
std["Sem"]=3
std["College"]="BGSP"
print("The student dictionary after inserting sem and college is : ",std)
std["name"]="N.S"
print("The student dictionary after changing Name is : ",std)
del std["branch"]
print("The student dictionary after deleting branch is :",std)
std.pop("regno")
print("The student dictionary after removing Regno is :",std)

