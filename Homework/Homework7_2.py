# x,y are respectively local and global variables for each function
def func1():
    x=20
    global y
    y=10
    print(f'sum x,y for func1:{x+y}')
    
def func2():
    x=36
    global y
    y=5
    print(f'sum x,y for func2:{x+y}')
#Because y is a global variable in both functions  , It takes its value into the function that was last called
func1()
print(f"y value:{y}")
func2()
print(f"y value:{y}")
#Because x is a local variable in both functions, it cannot be called  #print(x+10)
