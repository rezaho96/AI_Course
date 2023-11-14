# def fun1(n):
#     return n+500
# list1=[50,6,2,3,54,10]
# print(list(map(fun1,list1)))

# list1=[50,6,2,3,54,10]
# print(list(map(lambda x:x/20,list1)))

# list1=[50,6,2,3,54,10]
# print(list(map(str,list1)))

# list1=[50,6,2,3,54,10]
# list(map(print,list1))

aliScore=[18,20,13,18,16,14]
rezaScore=[11,16,17,19,16,12]
mehdiScore=[10,18,11,20,15,18]
print(list(map(lambda *args:sum(args)/len(args),aliScore,rezaScore,mehdiScore)))