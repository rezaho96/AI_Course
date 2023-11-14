import collections
class Mystring(collections.UserString):
    def insert(self,index,str):
        list1=[]
        for i in self.data:
            list1.append(i)
        list1.insert(index,str)
        self.data="".join(list1)
    
    def reverse(self):
        list1=[]
        for i in self.data:
            list1.append(i)
        list1.reverse()
        self.data="".join(list1)
        
# -----------------main---------------------
name=Mystring("ali adeghi")
name.insert(4,"s")
print(name)

str1=Mystring("hhh mmm aaa")
str1.reverse()
print(str1)

