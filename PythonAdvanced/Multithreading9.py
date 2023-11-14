from threading import Thread,current_thread,enumerate,Lock,RLock
from time import sleep

counter=0
lock=RLock()


def fun1():
    global counter
    lock.acquire()
    fun2()
    counter+=1
    sleep(1)
    print(f"counter {current_thread().name} : {counter}")
    lock.release()
def fun2():
    global counter
    lock.acquire()
    counter-=1
    sleep(1)
    print(f"counter {current_thread().name} : {counter}")
    lock.release()
    
t1=Thread(target=fun1)

t1.start()
t1.join()

print(f"counter {current_thread().name} : {counter}")
print("The end....")