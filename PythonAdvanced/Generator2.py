# list1=[i for i in range(0,10)]
# print(list1)

# genr1=(i for i in range(0,10))
# print(genr1)
# for i in genr1:
#     print(i,end="\t")



list1=[i for i in range(0,10000)]
print(list1[0:10])

#تفاوت سریع تر حافظه کمتر
genr1=(i for i in range(0,10))
print(genr1)
for i in range(0,10):
    print(i,end="\t")



