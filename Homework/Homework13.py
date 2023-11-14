import numpy as np

with open("Homework\precipitation_Fall_2019.txt","r") as file1:
    precipitation_Fall_2019=file1.read().split("\n")
with open("Homework\precipitation_Fall_2020.txt","r") as file2:
    precipitation_Fall_2020=file2.read().split("\n")
with open("Homework\precipitation_Fall_2021.txt","r") as file3:
    precipitation_Fall_2021=file3.read().split("\n")
        
precipitation_Fall_2019=np.array(precipitation_Fall_2019).astype("float32").reshape(3,5)
average_precipitation_per_month_2019=np.mean(precipitation_Fall_2019,axis=1)

precipitation_Fall_2020=np.array(precipitation_Fall_2020).astype("float32").reshape(3,5)
average_precipitation_per_month_2020=np.mean(precipitation_Fall_2020,axis=1)

precipitation_Fall_2021=np.array(precipitation_Fall_2021).astype("float32").reshape(3,5)
average_precipitation_per_month_2021=np.mean(precipitation_Fall_2021,axis=1)

a1=average_precipitation_per_month_2019[np.newaxis]
a2=average_precipitation_per_month_2020[np.newaxis]
a3=average_precipitation_per_month_2021[np.newaxis]
array_2D=np.concatenate((a1,a2,a3),axis=0)
print(array_2D)

#-----------calculate the most precipitation-----
print(100*"*"+'\n'+"The most precipitation:")
most_precipitation=np.max(array_2D)
print(most_precipitation)
print(np.where(array_2D==most_precipitation))


#array_2D[2,2]
#بیشترین بارش مربوط به ماه آذر و سال 2021