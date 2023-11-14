import pandas as pd
import matplotlib.pyplot as plt

# read file and save to data frame format
df_A=pd.read_csv("Homework\product_A.csv")
df_B=pd.read_csv("Homework\product_B.csv")
df_C=pd.read_csv("Homework\product_C.csv")

# fill Nan data with zero value
df_A=df_A.fillna(0)

# concatenate three data frame A,B,C 
df_concat=pd.concat([df_A,df_B,df_C])

# group by max value
df_max_groupby_code=df_concat.groupby("Code")[["Name","View","Like","Order"]].max()


nrow=4
ncol=2
fig, axes = plt.subplots(nrow, ncol)
plt.subplots_adjust(wspace=0.2, hspace=0.7)
# Show max values("View","Like","Order) for A,B,C  
df_max_groupby_code.plot(kind="bar",x="Name",y="View",ax=axes[0,0],fontsize=5,color="red")
df_max_groupby_code.plot(kind="bar",x="Name",y="Like",ax=axes[0,1],fontsize=5,color="green")
df_max_groupby_code.plot(kind="bar",x="Name",y="Order",ax=axes[1,0],fontsize=5,color="pink")

# Show Order values for A,B,C
df_A.plot(kind="line",x="Day",y="Order",ax=axes[2,0],fontsize=4,color="#25FFFF",ylabel="A")
df_B.plot(kind="line",x="Day",y="Order",ax=axes[2,1],fontsize=4,color="#25FF2F",ylabel="B")
df_C.plot(kind="line",x="Day",y="Order",ax=axes[3,0],fontsize=4,color="#FFFF14",ylabel="C")
plt.show()


# پربازديدترين C
#  محبو بترين C
# پرفرو شترين B


#ََسفارش در انتهای ماه بیشتر بوده و پیک سفارش نیز در روزهای 17و30 ام است A برای محصول 
#ََسفارش در ابتدای ماه کمی بیشتر بوده و پیک سفارش نیز در روز 17 ام است B برای محصول 
#ََسفارش در ابتداوانتهای ماه تقریبا یکسان بوده و پیک سفارش نیز در روز 17 ام است C برای محصول 