# num=int(input("Enter number: "))
# assert num>=100 ,"number is less than 100"
# print(num)




# def div(num1,num2):
#     assert num2!=0,"num2 shoud not be zero"
#     return num1/num2

# div(5,0)


names=[]
def add_name(name):
    assert name not in names , name+" is Repetitious"
    names.append(name)
    
add_name("ali")
add_name("hasan")
add_name("reza")
add_name("mahtab")
add_name("mahtab")
add_name("saeid")