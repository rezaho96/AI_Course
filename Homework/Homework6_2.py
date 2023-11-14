def remove(func1):
    # Remove negative and float numbers
    def func2(list):
        list2=[]
        for i in list:
            if i >= 0 and isinstance(i,int):
                list2.append(i)
        return func1(list2)
    return func2
@remove
def factorial(list1):
    list2=[]
    for i in list1:
        factorial=1
        for j in range(1,i+1):
           factorial*=j
        list2.append(factorial)
    return list2 
#--------------main-----------------  
number_List = [4, 3, 8, 0, -3, -45, 2, 10, -16, 23, 9, 1, -6, 55, 3.4, 6, 11.5]
list1=[2,4,5,0,1]
print(factorial(number_List))