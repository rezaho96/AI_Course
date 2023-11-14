import os
print(os.getcwd())
if not os.path.exists(r"Homework\Newfolder"):
    os.mkdir(r"Homework\Newfolder")
# Modify the text 
try:
    with open(r"Homework\files_in_python.txt","r") as files_in_python ,open(r"Homework\Newfolder\files_in_python_edit.txt","w") as files_in_python_edit:
        for line in files_in_python.readlines():
            line=line.replace("inbuilt","built-in")
            files_in_python_edit.write(line)
    files_in_python.close()
    files_in_python_edit.close()             
except Exception as error:
    print("Error:",error)

# ------------------------
files_in_python_size=os.path.getsize(r"Homework\files_in_python.txt")/1024
files_in_python_name=os.path.basename(r"Homework\files_in_python.txt")
lines1=[f"File Name: {files_in_python_name}",f"\nFile Size: {files_in_python_size}KB"]
# Save the modified file information in another file
try:
    with open("Homework/Newfolder/description.txt","w+") as descriptionFile:
        descriptionFile.writelines(lines1)
        descriptionFile.seek(0)
        print(descriptionFile.read())
    descriptionFile.close()
except Exception as error:
    print("Error:",error)
    