# list1=[2,1,4,5,4]
# print(list1)
# print(*list1)


# list2=[1,14,[5,4,7],7]
# print(list2)
# print(*list2)


# def func(*args):
#     print(args)
# list1=[2,6,7,4]
# func(list1,5)
# func(*list1,5)


# def func(**kwargs):
#     print(kwargs)

# func(x=10,y=20)
# dic1={"a":5,"n":9}
# func(**dic1)


def func(ali,reza,saeid):
    print(ali)
    print(reza)
    print(saeid)
    
dic1={"ali":5,"reza":6,"saeid":1}
func(**dic1)