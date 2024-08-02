import pandas as p
s=p.Series(['abc','cs001','cse','bgsp','male'],index=['name','regno','branch','college','gender'])
print(s)
print("first :\n",s.head(3))
print("last :\n",s.tail(3))
print("2nd :\n",s[2])
print("2 - 5:\n",s[2:5])
print("name :\n ",s['name'])
print("ns :\n",s[['name','regno']])
