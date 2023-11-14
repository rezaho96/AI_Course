from threading import Thread,current_thread,enumerate
from time import sleep


def fun(name):
    print("start " + name)
    print(enumerate())
    for thread in enumerate():
        print(thread.name)
    sleep(4)
    print("End " + name)
    


t1=Thread(target=fun,args=["Ali"],name="T1")
t2=Thread(target=fun,args=["Mohamad"],name="T2")

t1.start()
t2.start()

t1.join()
t2.join()

print("The end....")