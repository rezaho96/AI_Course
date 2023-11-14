#title join split lower upper len startswith endswith strip rjust ljust center isdigit isnumeric

# name="reza hoseini"
# print(name.title())

# name="reza hoseini"
# print(len(name))

# name="reza HOSEINI"
# print(name.lower())
# print(name.upper())
# print(name)

# str1="gdhfkd; kajgfr yroiiod dmng ealtrn"
# list1=str1.split(" ")
# print(list1)

# list2=["ali","saeid","davood","mahmood"]
# print('_'.join(list2))

# name="reza hoseini"
# print(name.startswith("re"))
# print(name.endswith("ni"))

# str2="  jldsfkffffffffffff   lsdkgjd   lkdjf  djg  "
# print("*"+str2+"*")
# print("*"+str2.strip()+"*")

# name="reza hoseini"
# print(name.ljust(30,"_"))
# print(name.rjust(30,"_"))
# print(name.center(30,"_"))

#isdigit اعدداد isnumber اعداد +یونی واحدها
print("569".isdigit(),"569".isnumeric())
print("56/9".isdigit(),"56/9".isnumeric())
print("56a9".isdigit(),"56a9".isnumeric())
print("56.9".isdigit(),"56.9".isnumeric())
print("¼".isdigit(),"¼".isnumeric())


print("\u0030")
print("\u0036")