import pandas as pd
import numpy as np

date1=pd.date_range("20180206",periods=6)
df1=pd.DataFrame(np.random.randn(6,4),index=date1,columns=list("ABCD"))
print(df1)

print("****************")
print(df1["A"])

print("****************")
print(df1[0:4])
print("****************")
print(df1["2018-02-06":"2018-02-08"])
print("****************")
# Selection by label
print(df1.loc[date1[0]])
print("****************")
print(df1.loc[date1[0],"A"])
print("****************")
print(df1.loc[date1[0],["A","B"]])
print("****************")
print(df1.loc[:,["A","D"]])
print("****************")
print(df1.loc["2018-02-06":"2018-02-08",["A","D"]])
print("****************")

# Selection by index
print(df1.iloc[1,3])
print("****************")
print(df1.iloc[[1,2,3],3])
print("****************")
print(df1.iloc[:,2])
print("****************")
print(df1.iloc[1:2,0:1])
print("****************")

print(df1.iloc[[1,2,3],[0,3]])
print("****************")
print(df1.iat[1,1])

# ////////////////////////////
print("****************")
print(df1[df1>0])
print("****************")
print(df1[df1["A"]>0])

df2=df1.copy()
df2["E"]=["one","two","three","four","five","sex"]
print(df2[df2["E"].isin(["two","four"])])

df2.at["2018-02-07",'E']="two*"
df2.iat[2,4]="three*"
df2.loc["2018-02-09","E"]="five*"
df2.iloc[[0,3,5],4]=["one*","four*","sex*"]
print(df2)
# ///////////////////////////////

df3=df1.reindex(index=date1[0:4],columns=list(df1.columns)+["E"])
print(df3)
df3.iloc[2,4]=3
print(df3.dropna(how="any"))
df4=df3.fillna(value=8)
print(df3)
print(df4)
print(df3.isna())
print(df4.isna())