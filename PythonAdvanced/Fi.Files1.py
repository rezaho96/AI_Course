# file1=open("PythonAdvanced/myfiles/file1.txt","r")
# print(file1.tell())
# print(file1.read())
# print(file1.tell())
# file1.close()

# file1=open("PythonAdvanced/myfiles/file1.txt","r")
# print(file1.tell())
# print(file1.readline())
# print(file1.tell())
# file1.close()

# file1=open("PythonAdvanced/myfiles/file1.txt","r+")
# print(file1.tell())
# file1.seek(12,0)
# print(file1.readline())
# file1.seek(10,0)
# file1.write("*****mm")
# print(file1.tell())
# file1.close()


# file1=open("PythonAdvanced/myfiles/file1.txt","r+")
# print(file1.tell())
# file1.seek(10,2)#??!!
# print(file1.readline())
# print(file1.tell())
# file1.close()


# file1=open("PythonAdvanced/myfiles/file1.txt","rb")
# print(file1.tell())
# file1.seek(5,1)
# print(file1.readline())
# print(file1.tell())
# file1.close()


# file1=open("PythonAdvanced/myfiles/file1.txt","rb")
# print(file1.tell())
# file1.seek(-14,2)
# print(file1.readline())
# print(file1.tell())
# file1.close()


file1=open("PythonAdvanced/myfiles/file1.txt","rb")
print(file1.read(15))
print(file1.name)
print(file1.mode)
print(file1.closed)
file1.close()
print(file1.closed)