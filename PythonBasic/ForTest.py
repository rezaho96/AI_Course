from re import I


a= int(input("Enter number1 :"))
b= int(input("Enter number2 :"))
s=1
for i in range(a+1,b,1):
	s*=i
print(s)
