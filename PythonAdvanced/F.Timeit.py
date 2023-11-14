import timeit
#این روش دقیق نیست
# startTime=timeit.default_timer()
# x=20*444444+50000
# stopTime=timeit.default_timer()
# print(stopTime-startTime)

#دقیق تر

print(timeit.timeit(setup="y=1000;z=12000",stmt="x=50*y*z"))
print(timeit.timeit(setup="y=1000;z=12000",stmt="x=50*y*z",number=2))
setup="import random"
myCode='''
list1=[]
def func():
    for i in range(500):
        list1.append(random.randint(0,100))
    
'''
print(timeit.timeit(setup=setup,stmt=myCode))
print(timeit.timeit(setup=setup,stmt=myCode,number=10))


print(timeit.repeat(setup=setup,stmt=myCode,repeat=4))
print(timeit.repeat(setup=setup,stmt=myCode,repeat=4,number=10))