from threading import Thread
from time import sleep


def fun(name,delay):
    print("start " + name)
    for i in range(1,11):
        sleep(delay)
        print(name +"_" +str(i))
    print("End " + name)
    


t1=Thread(target=fun,args=["Ali",.3])
t2=Thread(target=fun,args=["Mohamad",.5])

t1.start()
t2.start()

t1.join()
t2.join()

print("The end....")