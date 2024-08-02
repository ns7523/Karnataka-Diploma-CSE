d1={"name":"akash","regno":"498cs21047","branch":"cse"}
print(d1)
print("STUDENT NAME IS :",d1["name"])
print("REGISTER NO : ",d1["regno"])
d1["sem"]=3
d1["college"]="bgsp"
print(d1)
d1["name"]="NS"
print(d1)
del d1["branch"]
print(d1)
d1.pop("regno")
print(d1)
