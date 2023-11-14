try:
    x=int(input("Enter number1:"))
    y=int(input("Enter number2:"))
    print(x/y)

    #open("file1.txt","r")

    n=int("12d4")
    print(n)
except ZeroDivisionError as error:
    print(error)
except FileNotFoundError as error:
    print(error)
except ValueError as error:
    print(error)
except :
    print("Error")
else:
    print("run is succesfuly")
finally:
    print("final...")
