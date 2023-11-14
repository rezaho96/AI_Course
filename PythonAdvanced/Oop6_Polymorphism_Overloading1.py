print(len("ali"))
print(len([2,5,6,4,1,4]))
print(5+6)
print(2.2+8.1)
print("ali"+"reza")
print(5*3)
print(5*"\thasaan")

# def sum(x,y=0,z=0):
#     return x+y+z

# print(sum(2,5,6))
# print(sum(2,5))
# print(sum(2))


from multipledispatch import dispatch
@dispatch(int,int)
def sum(x,y):
    return x+y

@dispatch(int,int,int)
def sum(x,y,z):
    return x+y,z

print(sum(6,8,9))
print(sum(5,3))