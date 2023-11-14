import pandas as pd
import matplotlib.pyplot as plt

# خواندن داده ها از فایل و تبدیل به دیتافریم
df = pd.read_csv('./Homework/data.csv')

# محاسبه میانگین درآمد هر فرد
df['Average Income'] = df.iloc[:, 10:].mean(axis=1)

# رسم نمودار میله‌ای میانگین درآمد هر فرد
plt.bar(df['Name'], df['Average Income'])
plt.xlabel('Name')
plt.ylabel('Average Income')
plt.title('Average Income per Person')
plt.xticks(rotation=45)
plt.show()

# رسم نمودار خطی روند تغییر درآمد هر فرد در ۱۲ ماه سال
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
for index, row in df.iterrows():
    plt.plot(months, row[11:], label=row['Name'])

plt.xlabel('Month')
plt.ylabel('Income')
plt.title('Income Trend per Person')
plt.legend()
plt.xticks(rotation=45)
plt.show()