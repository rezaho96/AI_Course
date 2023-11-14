import pandas as pd
import numpy as np
from scipy import stats

# خواندن داده ها از فایل و تبدیل به دیتافریم
df = pd.read_csv('./Homework/data_1.csv')
print(df)
print(80*'-')
# محاسبه میانگین و میانه برای ستون‌های سن و وزن
age_mean = df['Age'].mean()
age_median = df['Age'].median()

weight_mean = df['Weight'].mean()
weight_median = df['Weight'].median()

print('Age Mean:', age_mean)
print('Age Median:', age_median)
print('Weight Mean:', weight_mean)
print('Weight Median:', weight_median)

# محاسبه مد برای ستون‌های قد، جنسیت و مدرک تحصیلی
height_mode = df['Height'].mode()[0]
gender_mode = df['Gender'].mode()[0]
education_mode = df['Education'].mode()[0]

print('Height Mode:', height_mode)
print('Gender Mode:', gender_mode)
print('Education Mode:', education_mode)
print(80*'-')
# محاسبه بازه برای ستون‌های سن، قد و وزن
age_range = df['Age'].max() - df['Age'].min()
height_range = df['Height'].max() - df['Height'].min()
weight_range = df['Weight'].max() - df['Weight'].min()

print('Age Range:', age_range)
print('Height Range:', height_range)
print('Weight Range:', weight_range)
print(80*'-')
# محاسبه واریانس و انحراف معیار برای ستون‌های سن، قد و وزن
age_variance = df['Age'].var()
age_stddev = df['Age'].std()

height_variance = df['Height'].var()
height_stddev = df['Height'].std()

weight_variance = df['Weight'].var()
weight_stddev = df['Weight'].std()

print('Age Variance:', age_variance)
print('Age Standard Deviation:', age_stddev)
print('Height Variance:', height_variance)
print('Height Standard Deviation:', height_stddev)
print('Weight Variance:', weight_variance)
print('Weight Standard Deviation:', weight_stddev)
print(80*'-')
# محاسبه کارتیل‌های اول، دوم و سوم برای ستون‌های سن، قد و وزن
age_q1, age_q2, age_q3 = np.percentile(df['Age'], [25, 50, 75])
height_q1, height_q2, height_q3 = np.percentile(df['Height'], [25, 50, 75])
weight_q1, weight_q2, weight_q3 = np.percentile(df['Weight'], [25, 50, 75])

print('Age Quartiles:', age_q1, age_q2, age_q3)
print('Height Quartiles:', height_q1, height_q2, height_q3)
print('Weight Quartiles:', weight_q1, weight_q2, weight_q3)

print(80*'-')
#  محاسبه برای ستون‌های سن، قد و وزنIQR
age_iqr = stats.iqr(df['Age'])
height_iqr = stats.iqr(df['Height'])
weight_iqr = stats.iqr(df['Weight'])

print('Age IQR:', age_iqr)
print('Height IQR:', height_iqr)
print('Weight IQR:', weight_iqr)
print(80*'-')