from threading import Thread,Timer,current_thread
from time import sleep


def fun(name):
    print(current_thread().name)
    print("Hello   " + name)
  
    


t1=Timer(5,function=fun,args=["Ali"])
t1.start()
t1.join()

print("The end....")