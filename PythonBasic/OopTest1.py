#برنامه نویسی ساخته یافته-تابع-مبتنی بر عمل و تابع-توسعه برنامه سخت است-چه کارهایی باید انجام دهیم؟
#شی گرا-مبتنی بر داده-توسعه راحت تر1-قراره با چه داده هایی کار کنیم2-جه کار هایی باید روی داده انجام دهیم
#کلاس دارای ویژگی های و عملکرد های مشترک
#صفت های مشترک دانشجو(نام شماره دانشجویی کدملی تلفن و...)عملکرد های مشترک(ورود به سیستم-انتخاب واحدو...)
#اعضای کلاس : اعضای داده ای-اعضای تابعی- تابع سازنده -تابع اس تی ار-کلاس ورییبل ها
class Car:
    count=0
    def __init__(self,color,brand,price,maxSpeed,capacity):
        self.color=color
        self.brand=brand
        self.price=price
        self.maxSpeed=maxSpeed
        self.capacity=capacity
        Car.count+=1

    def __str__(self):
        return f"color:{self.color}\tbrand:{self.brand}"
    
    def stopEngine(self):
        print("stop")
    def startEngine(self):
        print("start")


print(Car.count)
car1=Car("white","pegho",2800,360,8)
car2=Car("red","prid",2000,160,4)
car3=Car("blue","jac",2900,380,6)
print(Car.count)
Car.count=8
print(Car.count)
print(car3,car3.capacity)
car2.startEngine()
car1.stopEngine()
        