from threading import Thread
from time import sleep


def fun(name):
    print("start " + name)
    sleep(4)
    print("End " + name)    
    
#/////////////////////////////
class MyThread(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
    
    def run(self):
        fun(self.name)
#//////////////////////////////
t1=MyThread("Ali")
t2=MyThread("Mohamad")

t1.start()
t2.start()

t1.join()
t2.join()

print("The end....")