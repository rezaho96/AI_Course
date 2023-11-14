import pandas as pd
import numpy as np

print(list(zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    )))
tuples=list(zip(
        ["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"],
        ["one", "two", "one", "two", "one", "two", "one", "two"],
    ))
index=pd.MultiIndex.from_tuples(tuples,names=["first","second"])
df=pd.DataFrame(np.random.randn(8,2),index=index,columns=["A","B"])
print(df)
# ----------------------stack----------------
print("***********")
df2=df[:4]
print(df2)
print("***********")
stacked=df2.stack()
print(stacked)
print("***********")
print(stacked.unstack())
print("***********")
print(stacked.unstack(0))
print("***********")
print(stacked.unstack(1))
print("***********")
print(stacked.unstack(2))

# ---------------------------Pivot Tables---------
print("*****************")
df = pd.DataFrame(
    {
        "A": ["one", "one", "two", "three"] * 3,
        "B": ["A", "B", "C"] * 4,
        "C": ["foo", "foo", "foo", "bar", "bar", "bar"] * 2,
        "D": np.random.randn(12),
        "E": np.random.randn(12),
    }
)
print(df)
print("*****************")
print(pd.pivot_table(df,values="E",index=["A","B"],columns="C"))

# --------------------TimeSeries-----------------------
print("*****************")
rng = pd.date_range("1/1/2012 00:00", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts_resample=ts.resample("1Min").sum()
print(ts_resample)
rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts = pd.Series(np.random.randn(len(rng)), rng)
ts_utc=ts.tz_localize("UTC")
ts_tzconv=ts_utc.tz_convert("US/Eastern")
print("******************")
print(ts_utc)
print("******************")
print(ts_tzconv)
print("******************")
rng = pd.date_range("3/6/2012", periods=5, freq="M")
ts = pd.Series(np.random.randn(len(rng)), index=rng)
ps=ts.to_period()
print(ps)
print(ps.to_timestamp())
prng = pd.period_range("1990Q1", "2000Q4", freq="Q-NOV")
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq("M", "e") + 1).asfreq("H", "s") + 9
print(ts.head())

# ---------------------Categorical-----------
df = pd.DataFrame(
    {"id": [1, 2, 3, 4, 5, 6], "raw_grade": ["a", "b", "b", "a", "a", "e"]}
)
df["grade"]=df["raw_grade"].astype("category")
print(df["grade"])
new_category=["very good","good","very bad"]
df["grade"]=df["grade"].cat.rename_categories(new_categories=new_category)
print(df["grade"])
df["grade"]=df["grade"].cat.set_categories(["very bad","bad","medium","good","very good"])
print(df["grade"])
print(df.sort_values(by="grade"))
print(df.groupby(["grade"]).size())
