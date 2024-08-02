import pandas as p
data={'name':['a','b','c','d','e'],'regno':[1,2,3,4,5],'age':[19,20,19,19,18],'marks':[100,100,100,100,100]}
df=p.DataFrame(data)
print("\n",df)
print("name : \n",df['name'])
print("\n",df[['name','marks']])
print(df.loc[1])
print(df.loc[1:3])
