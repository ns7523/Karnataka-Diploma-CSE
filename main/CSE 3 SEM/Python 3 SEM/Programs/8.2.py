from array import *
print("*** Array manipulation ***")
a=array("i",[50,20,30,10])
print("An array a : ",a)
print(a[2])
print(a[-2])
print(a[2:4])
print(a[:2])
print(a[2:])
a.append(40)
print("An array a after append : ",a)
a.extend([33,44,55])
print("An array a after extend : ",a)
a.insert(3,11)
print("An array a after insert : ",a)
a.pop()
print("An array a after pop : ",a)
a.remove(50)
print(a)
