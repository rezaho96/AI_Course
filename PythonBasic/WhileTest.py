num=int(input("Enter number:"))
n=0
while num>0:
    num//=10
    n+=1
print(f"N :{n}")

#print(54%10)