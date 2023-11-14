import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000), index=pd.date_range("1/1/2000", periods=1000))
ts = ts.cumsum()
# plt.figure(1)
# ts.plot()
# plt.show()
# //////////////////////////////////
df = pd.DataFrame(
    np.random.randn(1000, 4), index=ts.index, columns=["A", "B", "C", "D"]
)
df = df.cumsum()
# plt.figure()
# df.plot()
# plt.legend(loc='best')
# plt.show()
# --------------------csv-------------
df.to_csv("foo.csv")
print(pd.read_csv("foo.csv"))
# --------------------HDF5-------------
print("***********************")
df.to_hdf("foo.h5","df")
print(pd.read_hdf("foo.h5","df"))
# --------------------Excel-------------
print("****************************")
df.to_excel("foo.xlsx", sheet_name="Sheet1")
print(pd.read_excel("foo.xlsx", "Sheet1", index_col=None, na_values=["NA"]))