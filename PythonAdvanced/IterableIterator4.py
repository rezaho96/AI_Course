# start=0
# def getSubString(str):
#     return str[start]
# str1="abolfazl komaili"
# it_str1=iter(lambda:getSubString(str1),' ')
# for i in it_str1:
#     print(i)
#     start+=1



count=1
def counter():
    return count

it_count=iter(lambda:counter(),20)
for i in it_count:
    print(i)
    count+=1
