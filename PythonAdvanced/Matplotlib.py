import matplotlib.pyplot as plt
import numpy as np
# print(dir(plt))

# plt.plot([2,5,6,8])
# plt.ylabel("sum number")
# plt.show()


# plt.plot([2,5,6,8],[1,4,5,7])
# plt.show()


# plt.plot([2,5,6,8],[1,4,5,7],"ro")
# plt.axes([1,10,1,10])
# plt.show()


# a=np.arange(0,5,.5)
# plt.plot(a,a,"r--",a,a**2,"b*",a,a**3,"g^")
# plt.show()


# data={"a":np.arange(10),"d":np.random.randint(0,10),"c":np.random.randn(10)}
# data["d"]=np.abs(data["d"])*10+18
# data["b"]=data["a"]+10*np.random.randn(10)
# plt.scatter("a","b",c="c",s="d",data=data)
# plt.xlabel("entray a")
# plt.ylabel("entray b")
# plt.show()



# names=['group_1','group_2','group_3']
# values=[1,15,100]
# plt.figure(figsize=(10,3))
# plt.subplot(131)
# plt.bar(names,values)
# plt.subplot(132)
# plt.scatter(names,values)
# plt.subplot(133)
# plt.plot(names,values)
# plt.suptitle("Categorical Ploting")
# plt.show()


# def f(t):
#     return np.exp(-t)*np.cos(2*np.pi*t)
# t1=np.arange(0.0,5.0,.1)
# t2=np.arange(0.0,5.0,.02)
# # plt.figure()
# plt.subplot(211)
# plt.plot(t1,f(t1),"bo",t2,f(t2),"g")
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()




plt.figure(1)                
plt.subplot(211)             
plt.plot([1, 2, 3])
plt.subplot(212)             
plt.plot([4, 5, 6])
plt.figure(2)                
plt.plot([4, 5, 6])          
plt.figure(1)                                            
plt.subplot(211)                                         
plt.title('Easy as 1, 2, 3') 
plt.show()
