import json

# -----------------Serialize---------
person={
    "id":25,
    "age":22,
    "name":"ali",
    "family":"akbari"
}
people=[person,person,person]
jstr=json.dumps(person)
print(jstr)
print(type(jstr))
with open("PythonAdvanced\\myfiles\\file1.json","w") as file1:
    json.dump(people,file1,indent=4)
# ----------------------Deserialize------------

# str1='{\"id\":25,\"age\":22,\"name\":\"ali\",\"family\":\"akbari\"}'
# objDict=json.loads(str1)
# print(objDict)
str2='[{\"id\": 25,\"age\": 22,\"name\": \"ali\",\"family\": \"akbari\"},{\"id\": 13,\"age\": 12,\"name\": \"hasan\",\"family\": \"bagheri\"},{\"id\": 32,\"age\": 35,\"name\": \"sahel\",\"family\": \"fadaei\"}]'
objList=json.loads(str2)
for item in objList:
       print(item) 
print("*****************")
with open("PythonAdvanced\\myfiles\\file2.json","r") as file2:
    list1=json.load(file2)
    for item in list1:
        print(item)
        