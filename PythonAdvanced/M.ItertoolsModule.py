import itertools
import operator

print(dir(itertools))

print("********************************")

for i in itertools.count(0,8):
    if i>100:
        break
    print(i,end="-")
print()    
for i in itertools.cycle([5,6,9,8,20,14,18,14]):
    if i>15:
        break
    print(i,end=" ")
for i in itertools.cycle("fldsjgdjklgj"):
    if i=="j":
        break
    print(i,end=" ")
print()   
for i in itertools.repeat([4,5,6],3):
    print(i)

print("********************************")
print(list(itertools.product([1,2,3],["a","b","c"])))
print(list(itertools.product([1,2,3],repeat=3)))
print(list(itertools.product([1,2,3],"ali")))
print()
print(list(itertools.permutations([1,2,3],3 )))
print(list(itertools.permutations([1,2,3],2 )))
print(list(itertools.combinations([1,2,3],2 )))
print(list(itertools.combinations([1,2,3,4,5],2 )))
print(list(itertools.combinations_with_replacement([1,2,3,4,5],2 )))

print("********************************")
print(list(itertools.accumulate([1,2,8,6,3,4,1,5],func=operator.add)))
print(list(itertools.accumulate([1,2,8,6,3,4,1,5],func=operator.mod)))
print(list(itertools.accumulate([1,2,8,6,3,4,1,5],func=operator.mul)))


print("********************************")
list1=[2,5,4,4]
list2=["ali","hasan","saeid"]
list3=[{1:"h"},8]

print(tuple(itertools.chain.from_iterable([list1,list2,list3])))
str1="hjjs"
print(tuple(itertools.chain.from_iterable([list1,list2,list3,str1])))


print("********************************")
print(list(itertools.compress(list1,[0,1,0,1])))


print("********************************")
print(list(itertools.dropwhile(lambda x:x%2==0,list1)))
print(list(itertools.takewhile(lambda x:x%2==0,list1)))
print(list(itertools.filterfalse(lambda x:x%2==0,list1)))


print("********************************")
list1=[5,2,4,4,5,2,3,6,5,4,7]
print(list(itertools.islice(list1,2,8,2)))
print(list1[2:8:2])