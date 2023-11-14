from threading import Thread,current_thread
from time import sleep


def fun(name):
    print("start " + name)
    print(current_thread())
    print(current_thread().name)
    print(current_thread().ident)
    sleep(4)
    print("End " + name)
    


t1=Thread(target=fun,args=["Ali"],name="T1")
t2=Thread(target=fun,args=["Mohamad"],name="T2")

t1.start()
t2.start()

t1.join()
t2.join()

print("The end....")