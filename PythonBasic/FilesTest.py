#فایل ها به دو صورت : متنی و باینری
#read-write-append

# file1=open("E:/train/artificial intelligence/f1.txt","w")
# file1.write(f"reza\nsaeid\nmohamad\nkarim\nhamid")
# file1.close()

file1=open("E:/train/ArtificialIntelligence/f1.txt","a")
file1.write(f"abolfazl\nsajad\niman")
file1.close()


# file1=open("E:/train/artificial intelligence/f1.txt","r")
#str1=file1.read()
# print(str1)


# file1=open("E:/train/artificial intelligence/f1.txt","r")
# lines=file1.readlines()
# for line in lines:
#     print(line,end="")
# file1.close()

# import os
# if os.path.exists("E:/train/artificial intelligence/f2.txt") :
#     print("file is existed")
# else:
#     file1=open("E:/train/artificial intelligence/f2.txt","x")
#     file1.write("ali")
#     file1.close()


#آدرس دهی نسبی : برای انتقال فایل ها به سیستم های دیگر مناسب تر است

file1=open("PythonBasic/file/f2.txt","w")
file1.write(f"reza\nsaeid\nmohamad\nkarim\nhamid")
file1.close()
