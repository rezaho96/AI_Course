
# list1=[2,5,4,1,6,5]
# iter(list1)

# x=20
# iter(x)


# list1=[2,5,8,9,4,1]
# for i in list1:
#     print(i)


# str1="reza"
# iter(str1)

# list1=[1,2,5,4,7]
# itr_list1=iter(list1)
# for i in range(len(list1)):
#     print(next(itr_list1))

# str1="reza"
# itr_str1=iter(str1)
# while True:
#     try:
#         print(next(itr_str1))
#     except:
#         break


# def check_iterable(obj):
#     try:
#         iter(obj)
#         return True
#     except:
#         return False
    
# x=1
# y=2.3
# str1="jkl"
# list1=[201,5,4,"fkg"]
# tuple1=tuple(list1)
# set1={2,4,5,5,6}
# dic1={1:'sfjk',2:"fdsl"}

# print(check_iterable(x))
# print(check_iterable(y))
# print(check_iterable(str1))
# print(check_iterable(list1))
# print(check_iterable(tuple1))
# print(check_iterable(set1))
# print(check_iterable(dic1))


def check_iterable(obj):
    try:
        iter(obj)
        return True
    except:
        return False
class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __str__(self) -> str:
        return f"{self.name}\t{self.age}"
person1=Person("ali",25)
person2=Person("saeid",21)
list1=[person1,person2]
print(check_iterable(list1))
it_list1=iter(list1)
print(next(it_list1))
print(next(it_list1))