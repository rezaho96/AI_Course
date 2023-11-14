import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data=[1,2,5,5,7,2,3,4,2,4,1,9]

x_value=np.arange(len(data))
plt.figure(figsize=(13,5))
plt.plot(x_value,data,marker="*",linestyle='-',color='blue',label='Data')


# # محاسبه میانگین
# mean_value= np.mean(data)
# plt.axhline(mean_value,linestyle='dashed',color='red',linewidth=1,label='Mean')
# plt.text(x_value[-1] +1 ,mean_value,f'{mean_value:.2f}',color='red',verticalalignment='center')

# # محاسبه میانه
# median_value= np.median(data)
# plt.axhline(median_value,linestyle='dashed',color='green',linewidth=1,label='median')
# plt.text(x_value[-1] +1 ,median_value,f'{median_value:.2f}',color='green',verticalalignment='center')

# # محاسبه مد
# mode_value= stats.mode(data).mode[0]
# plt.axhline(mode_value,linestyle='dashed',color='purple',linewidth=1,label='Mode')
# plt.text(x_value[-1] +1 ,mode_value,f'{mode_value:.2f}',color='purple',verticalalignment='center')

# # محاسبه واریانس
# variance_value= np.var(data)
# plt.axhline(variance_value,linestyle='dashed',color='orange',linewidth=1,label='Variance')
# plt.text(x_value[-1] +1 ,variance_value,f'{variance_value:.2f}',color='orange',verticalalignment='center')

# # محاسبه انحراف معیار
# std_value= np.std(data)
# plt.axhline(std_value,linestyle='dashed',color='brown',linewidth=1,label='Std')
# plt.text(x_value[-1] +1 ,std_value,f'{std_value:.2f}',color='brown',verticalalignment='center')

# # محاسبه محدوده 
# data_range= np.ptp(data)
# plt.axhline(data_range,linestyle='dashed',color='black',linewidth=1,label='Range')
# plt.text(x_value[-1] +1 ,data_range,f'{data_range:.2f}',color='black',verticalalignment='center')

# محاسبه صدک ها 
# percentile= np.percentile(data,[20,30,40,50])
# plt.axhline(percentile[0],linestyle='dashed',color='magenta',linewidth=1,label='percentile[0]')
# plt.axhline(percentile[1],linestyle='dashed',color='cyan',linewidth=1,label='percentile[1]')
# plt.axhline(percentile[2],linestyle='dashed',color='blue',linewidth=1,label='percentile[2]')
# plt.axhline(percentile[3],linestyle='dashed',color='green',linewidth=1,label='percentile[3]')
# plt.text(x_value[-1] +1 ,percentile[0],f'20th percentile :{percentile[0]}',color='magenta',verticalalignment='center')
# plt.text(x_value[-1] +1 ,percentile[1],f'30th percentile :{percentile[1]}',color='cyan',verticalalignment='center')
# plt.text(x_value[-1] +1 ,percentile[2],f'40th percentile :{percentile[2]}',color='blue',verticalalignment='center')
# plt.text(x_value[-1] +1 ,percentile[3],f'50th percentile :{percentile[3]}',color='green',verticalalignment='center')

## محاسبه چارک ها 
qurtiles= np.percentile(data,[25,50,75])
plt.axhline(qurtiles[0],linestyle='dashed',color='magenta',linewidth=1,label='qurtiles[0]')
plt.axhline(qurtiles[1],linestyle='dashed',color='cyan',linewidth=1,label='qurtiles[1]')
plt.axhline(qurtiles[2],linestyle='dashed',color='blue',linewidth=1,label='qurtiles[2]')
plt.text(x_value[-1] +1 ,qurtiles[0],f'25th qurtiles :{qurtiles[0]}',color='magenta',verticalalignment='center')
plt.text(x_value[-1] +1 ,qurtiles[1],f'50th qurtiles :{qurtiles[1]}',color='cyan',verticalalignment='center')
plt.text(x_value[-1] +1 ,qurtiles[2],f'75th qurtiles :{qurtiles[2]}',color='blue',verticalalignment='center')

# # محاسبه انحراف معیار
q1= np.percentile(data,[25]) # محاسبه چارک اول
q3= np.percentile(data,[75]) # محاسبه چارک سوم
iqr= q3-q1 # محاسبه محدوده بین چارکی(IQR)
plt.axhline(iqr,linestyle='dashed',color='pink',linewidth=1,label='IQR')
plt.text(x_value[-1] +1 ,iqr,f'IQR :{iqr}',color='pink',verticalalignment='center')

plt.xticks(x_value)
plt.xlabel('Index')
plt.ylabel('Values')
plt.legend()
plt.tight_layout()
plt.show()
