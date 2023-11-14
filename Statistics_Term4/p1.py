import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data=[1,2,5,5,7,2,3,4,2,4,1,9]

sorted_data=np.sort(data) #مرتب سازی داده ها


mean_value= np.mean(data) # محاسبه میانگین
median_value= np.median(data) # محاسبه میانه
mode_value= stats.mode(data).mode[0] # محاسبه مد
var_value= np.var(data) # محاسبه واریانس
std_value= np.std(data) # محاسبه انحراف معیار
data_range= np.ptp(data) # محاسبه محدوده
percentile= np.percentile(data,[20,30,40,50]) # محاسبه صدک ها
qurtiles= np.percentile(data,[25,50,75]) # محاسبه چارک ها
q1= np.percentile(data,[25]) # محاسبه چارک اول
q3= np.percentile(data,[75]) # محاسبه چارک سوم
iqr= q3-q1 # محاسبه محدوده بین چارکی(IQR)

print(80*"*")
print("mean_value :\t\t",mean_value)
print("median_value :\t\t",median_value)
print("mode_value :\t\t",mode_value)
print("var_value :\t\t",var_value)
print("std_value :\t\t",std_value)
print("data_range :\t\t",data_range)
print("percentile :\t\t",percentile)
print("qurtiles :\t\t",qurtiles)
print("q1 :\t\t",q1)
print("q3 :\t\t",q3)
print("iqr :\t\t",iqr)
print(80*"*")
