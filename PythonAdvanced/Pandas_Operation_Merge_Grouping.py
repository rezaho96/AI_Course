import pandas as pd
import numpy as np
date1=pd.date_range("20180206",periods=4)
df=pd.DataFrame(np.random.randn(10,4))
s1=pd.Series([1,5,np.nan,14,np.nan,7,4,6,15,10],index=list(range(10)))
print(df)
print("**********")
print(df.mean())
print("**********")
print(df.mean(1))
print("**********")
print(df.sub(s1,axis=0))
print("**********")
print(df.sub(s1,axis=1))
print("**********")
print(df.sub(s1,axis="index"))
print("**********")
# ///////////////////////////////
print(df.apply(np.cumsum))
print("**********")
print(df.apply(lambda x:x.max()-x.min()))
print("**********")
print(df.apply(lambda x:x.max()-x.min(),axis=1))
# ////////////////////////////////
s2=pd.Series(np.random.randint(1,10,size=10))
print(s2.value_counts())
print("**********")
s3=pd.Series(["ali","Ahmad","hasan","HAMED"])
print(s3.str.upper())
print(s3.str.title())



# ---------merge---------------------------
print("**********")
print(df)
peices=[df[0:5],df[5:7],df[7:]]
print("**********")
print(pd.concat(peices))
print("**********")
left=pd.DataFrame({"key":["foo","loo"],"lval":[3,4]})
right=pd.DataFrame({"key":["foo","loo"],"rval":[8,7]})
print(pd.merge(right=right,left=left,on="key"))


# --------------Grouping----------
print("**********")
df = pd.DataFrame(
    {
        "A": ["foo", "bar", "foo", "bar", "foo", "bar", "foo", "foo"],
        "B": ["one", "one", "two", "three", "two", "two", "one", "three"],
        "C": np.random.randn(8),
        "D": np.random.randn(8),
    }
)
print(df.groupby("A")[["C"]].sum())
print(df.groupby("A").sum())
print(df.groupby("A").sum())
print(df.groupby("B").sum())
print(df.groupby("B")[["D"]].sum())
print(df.groupby(["B","A"])[["D"]].sum())
print(df.groupby(["A","B"])[["D","C"]].sum())