def func1():
    yield "reza"
    yield "mohamad"
    yield "saeid"
    yield "mahvash"

print(func1())

for i in func1():
    print(i)
f=func1()
print(next(f))
print(next(f))
print(next(f))
print(next(f))

