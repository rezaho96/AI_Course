# import numpy as np
# from scipy import stats
# import pandas as pd
# # ماتریس داده‌ها
# # data_matrix = np.array([[1, 2, 1], [3, 4, 2], [2, 2, 3]])
# df =pd.read_excel('Homework/New Microsoft Excel Worksheet.xlsx')
# df.columns=['A','B','C','D']
# df= df.fillna(100)
# data_matrix = df.values
# A=df['A']
# B=df['B']
# C=df['C']
# D=df['D']
# A=A.values
# B=B.values
# C=C.values
# D=D.values
# print(A)
# # محدوده اعدادی مورد نظر
# # min_value = 1
# # max_value = 3

# # تخمین تابع چگالی احتمال (PDF)
# pdf_estimate1 = stats.gaussian_kde(np.log(A.flatten()+1))
# # pdf_estimate1 = stats.gaussian_kde(np.log(A.flatten()+1))
# # pdf_estimate1 = stats.gaussian_kde(np.log(A.flatten()+1))
# # pdf_estimate1 = stats.gaussian_kde(np.log(A.flatten()+1))

# # تعداد نمونه‌های جدید
# num_samples = 106

# # تولید نمونه‌های جدید
# log_new_samples1 = pdf_estimate1.resample(size=num_samples)
# new_samples1 = np.exp(log_new_samples1)
# print(new_samples1)
# print(np.mean(A))
# import matplotlib.pyplot as plt

# plt.hist(new_samples1[0],density=True)
# plt.show()
# # تبدیل نمونه‌های جدید به ماتریس
# # new_samples_matrix = np.reshape(new_samples, (num_samples, data_matrix.shape[1]))

# # نمونه‌های جدید را با داده‌های اصلی ترکیب کنید
# # combined_matrix = np.vstack((data_matrix, new_samples_matrix))

# # print(combined_matrix)  
import numpy as np

# ساخت دنباله‌ی اعداد برای سیگنال sin با 100 نمونه
x_sin = np.linspace(-np.pi, np.pi, 100)
y_sin = np.sin(x_sin)

# تقسیم دنباله‌ی اعداد به 10 بازه‌ی مساوی با اندازه‌ی 2π/10
bins = np.linspace(-np.pi, np.pi, 101)
hist_sin, _ = np.histogram(y_sin, bins)

# محاسبه‌ی مقدار p برای هر بازه
p_sin = hist_sin / 100
print(p_sin)
print(x_sin)
print(bins)