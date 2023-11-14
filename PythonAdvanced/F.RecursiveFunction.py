def fibo(n):
    if n==0 or n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(10))

print("************************")

def printList(list1):
    if len(list1)==0:
        print(end="")
    else:
        print(list1[0],end="\t")
        printList(list1[1:])
        
list1=[5,4,8,96,2]
printList(list1)