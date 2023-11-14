#get  key  values  items   setdefault

dict1={"name":"reza","family":"hoseini","age":25,"avg":15}

print(dict1.get("name"))
print(dict1["name"])
print(dict1.get("color"))
print(dict1.keys())
print(dict1.values())
print(dict1.items())

str1="ali saeid mahdi siah davood karim"
dicChrNumber={}
for ch in str1:
    dicChrNumber.setdefault(ch,0)
    dicChrNumber[ch]+=1
print(dicChrNumber)
list1=sorted(dicChrNumber)
print(list1)
dict2={"na":""}
dict1.update(dict2)
print(dict1)