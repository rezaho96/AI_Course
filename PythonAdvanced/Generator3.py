def fibo(n):
    a=0
    b=1
    yield a
    yield b
    for i in range(n-2):
        a=b
        b=a+b
        yield b
    
for i in fibo(7):
    print(i)
