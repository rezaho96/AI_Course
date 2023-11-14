
class Product_Price:
    def __init__(self , product_Price_List):
        self.product_Price_List=product_Price_List

    def __add__(self,obj2):
        return [self.product_Price_List[i]+obj2.product_Price_List[i] 
               for i in range (0,len(self.product_Price_List))]

    def __sub__(self,number):
        return [self.product_Price_List[i]-number for i in range(0,len(self.product_Price_List))]
    
    def __mul__(self,number):
        return [self.product_Price_List[i]*number for i in range(0,len(self.product_Price_List))]

    def __truediv__(self,number):
        return [self.product_Price_List[i]/number for i in range(0,len(self.product_Price_List))]

    def __lt__(self,obj2):
        list1=[self.product_Price_List[i]<obj2.product_Price_List[i] 
               for i in range (0,len(self.product_Price_List))]
        if list1.count(True)>list1.count(False):
            return True
        else :
            return False
    
    def Avg(self,obj2):
        Discount_Sale=[(self.product_Price_List[i]+obj2.product_Price_List[i])/10 
               for i in range (0,len(self.product_Price_List))]
        Normal_Sale=[(self.product_Price_List[i]+obj2.product_Price_List[i])/2 
               for i in range (0,len(self.product_Price_List))]
        
        print(f"Average sales with discounts:{Discount_Sale}")
        print(f"Average normal sales:{Normal_Sale}")
        
## store 1 
product_Price_List1 = [5000,10000,15000,6000,25000,12000,14000,10000,7000,20000]
## store 2 
product_Price_List2 = [4000,12000,16000,5000,22000,10000,16000,11000,5000,18000]
p1=Product_Price(product_Price_List1)
p2=Product_Price(product_Price_List2)

print(p1+p2)
print(p1-2)
print(p1/2)
print(p1*2)
print(p1>p2)

p1.Avg(p2)

if p1<p2:
    print("Store 1 is more suitable")
else:
    print("Store 2 is more suitable")
    
