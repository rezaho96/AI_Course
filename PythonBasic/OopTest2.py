#ارزش کلاس ها:کپسوله سازی-چند ریختی-وراثت
#کپسوله سازی یعنی از بیرون به ویژگی ها یا توابع کلاس دسترسی نداشته باشیم و آن ها بصورت خصوصی تعریف شوند
class Worker:
    def __init__(self,name,lastName,age,meliCode):
        self.__name=name
        self.__lastName=lastName
        self.__age=age
        self.__meliCode=meliCode
    
    def __str__(self):
        return self.name +" "+self.lastName+" "+str(self.age)+" "+str(self.meliCode)
    
    def __func1():
        print("ok")
#.............................................
worker1=Worker("ali","sadeghi",25,8574)
#print(worker1.__name)#??
print(worker1.name)#??