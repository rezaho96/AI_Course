import re

# str1="ali-hasan-sajad-mahvash-iman"
# regex=re.search(r"sajad",str1)
# print(regex.group())


# str1="ali-hasan-sajad-mahvash-iman negin mahtab alireza"
# regex=re.search(r"m+\w+",str1)
# print(regex.group())



# str1="ali-hasan-sajad-mahvash-iman negin mahtab alireza"
# regex=re.findall(r"ali",str1)
# print(regex)



# str1="ali-hasan-sajad-mahvash-iman negin mahtab alireza"
# regex=re.findall(r"m+\w+",str1)
# print(regex)





# str1='''
# reza097@gmail.com
# alihom@gmail.com
# 2ghasem@gmail.com
# ghasem@email.com
# vahid@gmail.count
# 09174568888
# 09185748698
# 65035664400
# 091745866225
# 0913586478
# 091358a6478
# saber87@2gmail.com
# '''
# mobileNumber=re.findall(r"091\d{8}\s",str1)
# print(mobileNumber)

# emails=re.findall(r"[a-zA-Z].+@gmail\.com",str1)
# print(emails)

# emails_itr=re.finditer(r"[a-zA-Z].+@gmail\.com",str1)
# print(emails_itr)
# for i in emails_itr:
#     print(i.group())
    


# str1='''
# reza097@gmail.com
# alihom@gmail.com
# 2ghasem@gmail.com
# ghasem@email.com
# vahid@gmail.count
# 09174568888
# 09185748698
# 65035664400
# 091745866225
# 0913586478
# 091358a6478
# saber87@2gmail.com
# '''

# regex=re.sub("091\d{8}\s","***\n",str1)
# print(regex)




str1='''
Name is : reza - Age is : 22 - Avg is : 17.6
Name is : ali - Age is : 26 - Avg is : 15.6
Name is : saber - Age is : 30 - Avg is : 18.6
Name is : nima - Age is : 20 - Avg is : 14.6
'''
res=re.findall("Name is : (\w+) - Age is : (\d+) - Avg is : (\d+\.\d+)",str1)
print(res)
res2="name,age,avg"
res2+=re.sub("Name is : (\w+) - Age is : (\d+) - Avg is : (\d+\.\d+)","\g<1>,\g<2>,\g<3>",str1)
print(res2)