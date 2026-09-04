import pandas as pd
import random

# df=pd.DataFrame({
#     'df1':['a','b','c','d','e'],'df2':[1,2,3,4,5]
# })
# print(df)

# df=pd.DataFrame({'df1':random.randint(0,100)},index=[1,2,3,4,5])
# print(df)

# a=[1,2,3,4,5]
# s=pd.Series(a,index=["a","b",'c','d','e'])
# print(s)

# a={'a':1,"b":2,'3':3,'c':4}
# df=pd.Series(a)
# print(df)

# df=pd.Series(range(6))
# print(df)

d1=pd.DataFrame({'data1':[12,3,4,5,5,66],'data2':[5432,342,1212,4,5,3]})
d2=pd.DataFrame({'data1':[12,23,23,4,545,4],'data4':[67,565,656,5,65,6]})
df1=pd.merge(d1,d2,on=['data1'])
# print(d1)
# print(d2)
print(df1)