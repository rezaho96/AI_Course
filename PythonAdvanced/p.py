# print([1,2,3][:-2])
# print([i for i in [i for i in range(5)]][:-4])
# import operator
# res=operator.contains({'x':100,'x':200,'z':12},'y')
# print(operator.not_(res))
# import functools
# num=[0,1,2,3,5,8,13]
# r=filter(lambda x:x%2!=0,num)
# print(functools.reduce(lambda a,b:a+b,r))

# import re
# str1="hello my name is reza"

# res = re.finditer(r'hello',str1)
# for i in res:
#    print(i.group())

# res.group()
import numpy as np
print(np.zeros(5).dtype)