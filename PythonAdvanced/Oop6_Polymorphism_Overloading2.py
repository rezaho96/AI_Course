# عملگر ها در پایتون قابل توسعه هستند و می توان آن ها را دوباره برای شی ها تعریف کرد
# python standard operators as functionsسرچ

class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __add__(self,obj2):
        return self.age+obj2.age
    def __pow__(self,obj2):
        return self.age**obj2.age
    def __mul__(self,obj2):
        return self.age*obj2.age
"HGHDJ LAFGFHLKHG DAJDSLKG ALGGKL DAFLJSGK LAJDG LDGJDSK KJGDAKSGJ KGJDSA  LASDJGKL LAKSDGJ ks  lkdsjf dkfj dfsjkf kdlfsj jlfdsk kjsdfk kjskfd  sdkjfj skdjf ksjfkd jksdjf jksdf kjdfkj kdsjfk ksjdfk ksdjfk  ksfjdkdf jfkdsfjyewrieotu fiueitoy iewygoir  eiurioytkdh iewqyy  iewqyoiy ieryqtioy ieqwytioy"

person1=Person("saeid",1)
person2=Person("vahid",80)
print(person1+person2)
print(person1 ** person2)


