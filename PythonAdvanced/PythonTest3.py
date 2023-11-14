def sum(num1,num2):
    return num1+num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    if num2==0:
        raise ZeroDivisionError("Diviation by zero")
    return num1/num2
