from threading import Thread
from time import sleep


def fun(name):
    print("start " + name)
    sleep(4)
    print("End " + name)
    


t1=Thread(target=fun,args=["Ali"])
t2=Thread(target=fun,args=["Mohamad"])

t1.start()
t2.start()

t1.join()
t2.join()

print("The end....")