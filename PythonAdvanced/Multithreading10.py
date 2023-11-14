from threading import Thread,current_thread,enumerate,Lock,RLock,Semaphore,BoundedSemaphore
from time import sleep

counter=0
# lock=Semaphore(value=3)
lock=BoundedSemaphore(value=2)
# در این جا سمافور و بانددسمافور برعکس عمل می کنند یعنی سمافور مشکل را حل می کند

def fun1():
    global counter
    lock.acquire()
    counter+=1
    sleep(2)
    print(f"counter {current_thread().name} : {counter}")
    lock.release()
    # lock.release()

thread_list=[]
for i in range(8):
    thread_list.append(Thread(target=fun1))
for i in range(8):
    thread_list[i].start()
for i in range(8):
    thread_list[i].join()
    
print("The end....")