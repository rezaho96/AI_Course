from threading import Thread
from concurrent.futures import ThreadPoolExecutor
from time import sleep


def fun(name,family):
    print("start " + name +" " +family)
    sleep(4)
    print("End " + name + " " + family)
    
with ThreadPoolExecutor(max_workers=2) as executor:
    names=["Ali","Hasan","Mahdi","vahid","kazem"]
    families=["sadeghi","mohamadi","shokohi","atashrooz","ahmadi"]
    executor.map(fun,names,families)

print("The end....")