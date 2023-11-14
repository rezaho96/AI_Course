# func=lambda x,y,funcName:funcName(x,y)
# print(f"{func(5,6,lambda num1,num2:num1+num2)}")
#لامبداا توابعی که برای موقعی استفاده می شوند که یک خط کد داشته باشیم و بخواهیم خروجی سریع بگیریم
# func=lambda x,y,funcName:funcName(x,y)
# print(f"{(lambda x,y,funcName:funcName(x,y))(5,6,lambda num1,num2:num1+num2)}")

diclist=[{"Name":"ali","LastName":"shekohi","Age":25},
{"Name":"karim","LastName":"sajadi","Age":32},
{"Name":"mohamad","LastName":"memar","Age":16},
{"Name":"asad","LastName":"ahmadi","Age":12}]
print(sorted(diclist,key=lambda dic:dic["Name"]))
print(sorted(diclist,key=lambda dic:dic["LastName"]))