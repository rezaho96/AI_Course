from datetime import time,date,datetime,timedelta
import pytz

# time1=time(20,32,25,2000)
# print(time1)
# date1=date(1998,12,23)
# print(date1)
# print(date.today)
# print(datetime.now)
# datetime1=datetime(2021,3,24,12,23,12)
# print(datetime1)
# print(datetime1.year)
# print(datetime1.month)
# print(datetime1.day)
# print(datetime1.hour)
# print(datetime1.minute)
# print(datetime1.second)
# print(datetime1.microsecond)


# print(datetime.now())
# print(datetime.utcnow())


# print(datetime.now())
# print(datetime.now().strftime("%Y/%m/%d %H:%M:%S:%f"))
# print(datetime.now().strftime("%Y/%B/%d %H:%M:%S:%f"))
# print(datetime.now().strftime("%Y/%b/%d %H:%M:%S:%f"))



# datetime2=datetime.strptime("2003/2/13","%Y/%m/%d")
# print(datetime2)
# print(datetime2.year)
# print(datetime2.month)
# print(datetime2.day)


# datetime3=datetime.strptime("2015-2-13 11:36:20:2","%Y-%m-%d %H:%M:%S:%f")
# print(datetime3)
# print(datetime3.year)
# print(datetime3.month)
# print(datetime3.day)
# print(datetime3.hour)
# print(datetime3.minute)
# print(datetime3.second)
# print(datetime3.microsecond)


# print(datetime.now())
# print(datetime.utcnow())
# print(datetime.now(pytz.timezone("Asia/Tehran")))
# print(datetime.now(pytz.timezone("Us/Central")))


# time1=datetime(2013,10,24,14,14,55)
# time2=datetime(2020,5,1,1,4,5)
# timedelta1=timedelta(2,2,0,0,5,2,3)
# time3=time1+timedelta1
# print(time3)


time1=datetime(2019,10,24,14,14,55)
time2=datetime(2020,5,1,1,4,5)

sectime=abs(time1-time2).total_seconds()
mintime=abs(time1-time2).total_seconds()/60
hourtime=abs(time1-time2).total_seconds()/(60*60)
daytime=abs(time1-time2).total_seconds()/(60*60*24)
print(sectime)
print(mintime)
print(hourtime)
print(daytime)

import tensorflow as tf
tf.keras.layers.Dense()