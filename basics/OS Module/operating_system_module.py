import os
#print(dir(os))
#print(os.getcwd()) #gives your operating_system_module.py file  program's working directory
#its not compulsory to be at the same directory where you are executing ,we can change the working directory as follows
#os.chdir("C:\\") #changing to c drive only
#print(os.getcwd())
try:
    f=open("kristal.txt")
except Exception as e:
    print(e)
    print("file cannot be succesfully opened")
    f=None
else:
    print("file opened successfully")
finally:
      if f:
        f.close()
#thus if i try to open the textfile present physically in the directory,it will show error because directory of the program file is virtually changed

#print(os.listdir()) #gives list of names of all the files of current working directory
#print(os.listdir("C://")) #gives list of names of all the files in C directory

#to make folders
#os.mkdir("kristal12")
#os.mkdir("folder/subfolder") #error it will show error because there is no folder file and you cant create sub folder

#to solve that folder
#os.makedirs("folder/subfolder")

#to know environment variable path
#print(os.environ.get('PATH'))

#To join two paths in an optimal way
#print(os.path.join("C://","/kristal.txt"))

#to know if a directory exists or not
print(os.path.exists("C://"))
print(os.path.exists("C://Program Files"))
print(os.path.exists("C://kristal"))

#to know if the given path is a file or directory
print(os.path.isdir("C://Program Files"))
print(os.path.isdir("C://Users/Kristal Shrestha/Desktop/python/basics/OS Module/kristal.txt"))
print(os.path.isfile("C://Program Files"))
print(os.path.isfile("C://Users/Kristal Shrestha/Desktop/python/basics/OS Module/kristal.txt"))



#other things search in google

