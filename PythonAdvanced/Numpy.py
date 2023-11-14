import numpy as np 
# print(dir(np))

# array1=np.array([2,5,6,4,7])
# print(array1)
# print(array1.shape)
# array2=array1.reshape(1,-1)
# print(array2)

# print(array1.ndim)
# print(array2.ndim)
# print(array1.dtype.name)
# print(type(array1))
# print(array1.size)
# print(array1.itemsize)

# //////////////////////////////////////////////////

# arry1=np.array([(2,5,6,8,7),(1,7,9,3,7)],dtype=complex)
# arry2=np.array([[2,5,6,8,7],[1,7,9,3,7]],dtype=float)
# print(arry1)
# print(arry2)

# //////////////////////////////////////////////////

array1=np.arange(1,10,2,dtype=int)
array2=array1[np.newaxis]
print(array2.shape)
print(array2.reshape(5,1,1))
print(array2.reshape(1,1,5))
# array2=np.arange(1,10,.2,dtype=float)
# array3=np.zeros((5,8),dtype=float)
# array4=np.zeros_like(array1)
# array5=np.ones((5,10),dtype=float)
# array6=np.ones_like(array2)
# array7=np.empty((5,6))
# array8=np.empty_like(array2)
# array9=np.linspace(.5,80.2,20)
# array10=np.fromfunction(lambda i, j: i + j, (3, 3), dtype=int)
# array11=np.logspace(1,2,10)
# list1=[array1,array2,array3,array4,array5,array6,array7,array8,array9,array10,array11]
# for i in list1:
#     print(i)
#     print("___________")
# array1.fill(8)
# print(array1)
# //////////////////////////////////////////////////////

# a1=np.random.default_rng(10)
# print(a1)
# a2=a1.random(23)
# print(a2)
# a3=np.random.rand(2,4,5)
# print(a3)
# a4=np.random.randint(1,10,20)
# print(a4)
# a5=np.random.random_sample(20)
# print(a5)
# a6=np.random.random(20)
# print(a6)
# a7=np.random.randn(1,2,3)
# a8=np.random.ranf(20)
# print(a7)
# print(a8)

# ///////////////////////////////////////////////////////

# a=np.arange(10,dtype=int)
# b=np.arange(0,5,.5,dtype=float)
# print(a+b)

# print(a**b)
# print(a-b)
# print(a/b)
# print(a//b)
# print(a<b)
# print(a.sum())
# print(a.min())
# print(a.max())
# print(a.std())
# print(a*b)
# print(np.multiply(a,b))
# print(a@b)
# print(np.dot(a,b))
# d=a.reshape(2,5)
# print(d.sum(axis=1)) #axis=1 column and axis=0 row
# print(d.mean(axis=0)) #axis=1 column and axis=0 row
# print(np.average(d,axis=0))
# print(d.std(axis=0)) #axis=1 column and axis=0 row
# print(np.exp(a))
# print(np.sqrt(a))
# print(np.add(a,b))
# ////////////////////////////////////////////////////

# a=np.random.randint(0,100,100).reshape(2,5,10)
# print(a)
# print(".....................")
# print(np.sort(a,axis=0))

# print("********************")
# print(np.argmax(a,axis=0))
# print("********************")
# print(np.argsort(a,axis=0))
# print("********************")
# print(np.argmin(a,axis=0))

# ///////////////////////////////////////////////////////

# x=np.arange(100)
# y=np.random.randint(1,100,100)
# print(x)
# print(y)
# print("x<y is:")
# print(np.where(x<y,x,10+y))
# print(x.reshape(10,10))
# print(np.all(x.reshape(10,10),axis=0))
# print(np.any(x.reshape(10,10),axis=0))
# a=np.array([[0,1,1,0,0],[1,1,1,1,0]])
# print(a)
# print(np.any(a,axis=0))
# print(np.all(a,axis=0))


# //////////////////////////////////////////

# a=np.fromfunction(lambda x,y:x*3+y ,(5,4),dtype=int)
# print(a)
# print(a[:3,:3])#row and column
# print(a[:,:3])
# print(a[:,0])
# print(a[:,2])
# print(a[-1])
# print(a[-1,:])
# print(a[:,-1])
# # 3D array
# b=np.reshape(a,(2,5,2))
# print(b[1,...])
# print(b[...,1])
# print(b[1:,2:,-1])

# print(b[:,np.newaxis])
# print(a[:,np.newaxis])
# # # نکته اگر تابع زیر دوبار استفاده شود بار دوم جواب درست نمی دهد
# for index , a in np.ndenumerate(a):
#     print(index,a)
# for index , b in np.ndenumerate(b):
#     print(index,a)