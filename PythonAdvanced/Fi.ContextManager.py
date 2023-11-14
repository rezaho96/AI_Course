# file1=open("PythonAdvanced/myfiles/file1.txt","a")
# file1.write("\n1")
# file1.close()

# file1=open("PythonAdvanced/myfiles/file1.txt","a")
# file1.readline()
# file1.close()

# try:
#     file1=open("PythonAdvanced/myfiles/file1.txt","a")
#     file1.readline()
#     file1.close()
# except Exception as error:
#     print("Error:",error)
# finally:
#     file1.close()

# with open("PythonAdvanced/myfiles/file1.txt","a") as file1:
#         try:
#           file1=open("PythonAdvanced/myfiles/file1.txt","a")
#           file1.readline()
          
#         except Exception as error:
#           print("Error:",error)
#         finally:
#             file1.close()
# print("The End...")


# try:
#     with open("PythonAdvanced/myfiles/file12.txt","r") as file1 ,open("PythonAdvanced/myfiles/backup.txt","w") as file2:
#         for line in file1.readlines():
#             file2.write(line)
#     file1.close()
#     file2.close()             
# except Exception as error:
#     print("Error:",error)

    
# try:
#     with open("PythonAdvanced/myfiles/file1.txt","r") as file1 ,open("PythonAdvanced/myfiles/backup.txt","w") as file2:
#         for line in file1.readlines():
#             file2.write(line)
#     file1.close()
#     file2.close()             
# except Exception as error:
#     print("Error:",error)


# class FileWritable:
#     def __init__(self,filepath,filemode):
#         self.filepath=filepath
#         self.filemode=filemode
    
#     def __enter__(self):
#         print("Start")
#         self.fileObject=open(self.filepath,self.filemode)
#         return self.fileObject
    
#     def __exit__(self,*exc):
#         if self.fileObject:
#             self.fileObject.close()
#         print("End...")

# with FileWritable("PythonAdvanced/myfiles/backup.txt","a") as file1:
#     print("Hello python..")


class Person:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def __str__(self):
        return f"{self.age}"
    
    def __enter__(self):
        print("start")
        return True
        
    def __exit__(self,*exc):
        print("End")
        return False
    
person2=Person("ahmad",100)
print(person2)
with Person("ali",25)as person1:
   print("")
   
    
        

    