import pandas as pd
import numpy as np
# print(dir(pd))

s=pd.Series([1,2,8,5,6,None,8])
print(s)

date1=pd.date_range("20180206",periods=6)
df1=pd.DataFrame(np.random.randn(6,4),index=date1,columns=list("ABCD"))
print(df1)

df2=pd.DataFrame({
    "A":pd.Timestamp("20210304"),
    "B":pd.Categorical(["train","test","train","test"]),
    "C":np.array([4]*4,dtype=float),
    "D":"flow",
    "E":1,
    "F":pd.Series(1,index=list(range(4)),dtype=int)
})
print(df2)
print(df2.dtypes)


#///////////////////////////////////////
print("***************************")
print(df1.head(2))
print(df2.head(2))
print("----")
print(df1.tail(3))
print(df2.tail(3))
print("----")
print(df1.columns)
print(df2.columns)
print("----")
print(df1.index)
print(df2.index)
print("----")
print(df1.to_numpy())
print(df2.to_numpy())
print("----")
print(df1.describe())
print(df2.describe())
print("----")
print(df1.T)
print(df2.T)
print("----")
print(df1.sort_index(1,ascending=False))
print(df2.sort_index(1,ascending=False))
print("----")
print(df1.sort_values(by="A"))
print(df2.sort_values("B"))