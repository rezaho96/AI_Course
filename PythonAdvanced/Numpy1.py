import numpy as np
# choices = [[0, 1, 2, 3], [10, 11, 12, 13],
#   [20, 21, 22, 23], [30, 31, 32, 33]]
# print(np.choose([2, 3, 1, 0], choices))
# print(np.choose([2, 4, 1, 0], choices, mode='clip')) # 4 goes to 3 (4-1)
# # because there are 4 choice arrays
# print(np.choose([2, 4, 1, 0], choices, mode='wrap')) # 4 goes to (4 mod 4)

# a = np.array([0, 1]).reshape((2,1,1))
# c1 = np.array([1, 2, 3]).reshape((1,3,1))
# c2 = np.array([-1, -2, -3, -4, -5]).reshape((1,1,5))
# print(np.choose(a, (c1, c2))) # result is 2x3x5, res[0,:,:]=c1, res[1,:,:]=c2


# //////////////////////////////////////////////////

# a = np.array([[1, 2], [3, 4], [5, 6]])
# print(np.compress([False,False,True],a,axis=0))
# print(np.compress([False,False,True,True],a))
# print(np.compress([0,1,1],a,axis=0))


# ///////////////////////////////////////////////////////

# rg=np.random.default_rng(10)
# print(10*rg.random((2,20)))
# a=np.floor(10*rg.random((2,20)))
# print(a)
# print(a.ravel())
# print(a.reshape((4,10)))
# b=a.reshape((4,10))
# print(b.shape)
# print(b.T.shape)
# b.resize((2,20))
# print(b)

# /////////////////////////////////////////////////////////

# rg=np.random.default_rng(10)
# a=np.floor(10*rg.random((3,5)))
# b=np.floor(10*rg.random((3,5)))
# print(a)
# print(b)
# print("***************")
# print(np.hstack((a,b)))
# print(np.vstack((a,b)))
# print(np.concatenate((a,b)))
# print(np.column_stack is np.hstack)
# print(np.row_stack is np.vstack)

# print(np.r_["r",np.array([1,2,3]),np.array([3,4,5])])
# print(np.r_["c",np.array([1,2,3]),np.array([3,4,5])])
# print(np.r_["1,2,0",np.array([1,2,3]),np.array([3,4,5])])
# print(np.r_["-1",np.array([1,2,3]),np.array([3,4,5])])
# print("*******************************")
# # print(np.c_["r",np.array([1,2,3]),np.array([3,4,5])])
# # print(np.c_["c",np.array([1,2,3]),np.array([3,4,5])])
# # print(np.c_["1,2,0",np.array([1,2,3]),np.array([3,4,5])])
# # print(np.c_["-1",np.array([1,2,3]),np.array([3,4,5])])

# //////////////////////////////////////////////////////////

# rg=np.random.default_rng(10)
# a=np.floor(10*rg.random((2,12)))
# print(a)
# print(np.hsplit(a,3))
# print(np.hsplit(a,(3,3)))
# print(np.hsplit(a,(2,3)))
# print(np.hsplit(a,(3,4)))

# ///////////////////////////////////////////////

a=np.arange(20).reshape((2,10))
b=a
print(b is a , id(a) , id(b))
c=a.view()
print(c is a)
print(c.base is a)
c=c.reshape((4,5))
print(a,"\n",c)
c[0,4]=555
print(a,"\n",c)
print("********************")
d=a[:,1:3]
d[:]=10
print(f"{d}\n{a}")

# Deep copy
print("---------------------------")
f=a.copy()
print(f is a)
print(f.base is a)
f[:]=5
print(f,"\n",a)