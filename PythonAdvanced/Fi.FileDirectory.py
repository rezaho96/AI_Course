import os
print(os.getcwd())
if not os.path.exists("PythonAdvanced/myfiles/Test1"):
    os.mkdir("PythonAdvanced/myfiles/Test1")

print(os.listdir("PythonAdvanced/myfiles"))
print(os.listdir())
if not os.path.exists("PythonAdvanced/myfiles/Test2"):
    os.mkdir("PythonAdvanced/myfiles/Test2")   

os.chdir("../")
print(os.getcwd())

#os.chdir("python_project/PythonAdvanced/myfiles/Test2") #خطا
os.chdir(r"python_project\PythonAdvanced\myfiles\Test2")
# or os.chdir(r"E:\train\ArtificialIntelligence\python_project\PythonAdvanced\myfiles\Test2")
if not os.path.exists("Test3"):
    os.mkdir("Test3") 
print(os.getcwd())
os.chdir("../")
os.chdir("../")
print(os.listdir())
for item in os.listdir():
    print("************")
    print(f"{item}:{os.path.isdir(item)}")
    
    print(f"{item}:{os.path.isfile(item)}")
os.chdir("../")
print(os.listdir())
for item in os.listdir():
    print("************")
    print(f"{item}:{os.path.isdir(item)}")
    
    print(f"{item}:{os.path.isfile(item)}")
print("########################################################################")   
print(os.path.basename("PythonAdvanced\Decorator1.py"))
print(os.path.normpath("PythonAdvanced\Decorator1.py"))
print(os.path.dirname("PythonAdvanced\Decorator1.py"))
print(os.path.realpath("PythonAdvanced\Decorator1.py"))

print(os.path.exists(r"PythonAdvanced\myfiles\file1.txt"))
print(os.path.lexists(r"PythonAdvanced\myfiles"))
print(os.path.lexists(r"PythonAdvanced\myfiles1"))


print(os.path.getctime(r"PythonAdvanced\myfiles\file1.txt"))
print(os.path.getmtime(r"PythonAdvanced\myfiles\file1.txt"))


print(os.path.getsize(r"PythonAdvanced\myfiles\file1.txt"))
print(os.path.getsize(r"PythonAdvanced\myfiles\file1.txt")/1024)
print(os.path.getsize(r"PythonAdvanced\myfiles\file1.txt")/(1024*1024))


print(os.path.join("E:\\","music","reza"))


s1=os.path.split(r"PythonAdvanced\myfiles\file1.txt")
print(s1)
print(s1[0])
print(s1[1])

s2=os.path.splitext(r"PythonAdvanced\myfiles\file1.txt")
print(s2)
print(s2[0])
print(s2[1])


import mimetypes
print(mimetypes.MimeTypes().guess_type("l1.jpg"))
print(mimetypes.MimeTypes().guess_type("l1.jpg")[0])
print(mimetypes.MimeTypes().guess_type("l1.jpeg")[0])
print(mimetypes.MimeTypes().guess_type("l1.png")[0])
print(mimetypes.MimeTypes().guess_type("l1.txt")[0])
print(mimetypes.MimeTypes().guess_type("l1.mp3")[0])
print(mimetypes.MimeTypes().guess_type("l1.mp4")[0])
print(mimetypes.MimeTypes().guess_type("l1.pdf")[0])


# os.remove(r"PythonAdvanced\myfiles\backup.txt")
os.rmdir(r"PythonAdvanced\myfiles\Test2\Test3")