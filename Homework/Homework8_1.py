import json,jmespath
import os
import operator
print(os.getcwd())
with open("Homework\employee.json","r") as file1:
    employes=json.load(file1)
Employe={}
Employe["employes"]=employes

# ***Names and family names of female employees in all companies***
print(50*"-")
print("Names and family names of female employees in all companies:")
print(jmespath.search("employes[?gender==`female`].fullName",Employe))
# ***Names and family names of male employees of Mapna company***
print(50*"-")
print("Names and family names of male employees of Mapna company:")
print(jmespath.search("employes[?gender==`male`] |  [?company== `MAPNA`].fullName",Employe))
# ***Names and surnames and e-mails of employees of Iran Khodro Company***
print(50*"-")
print("Names and surnames and e-mails of employees of Iran Khodro Company:")
print(jmespath.search("employes[?company== `Iran Khodro Co.`].{FullName:fullName,Email:email}",Employe))

# ***Full information of the first three people in terms of salary***
list_male=jmespath.search("employes[?gender==`male`].[fullName,gender,company,salary,email]  ",Employe)
print(list_male)
print(50*"*")
print("Full information of the first three people in terms of salary:")
print(sorted(list_male,key=operator.itemgetter(3),reverse=True)[0:3])

