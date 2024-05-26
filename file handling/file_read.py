file_pointer=open("kristal.txt","r")
# content=file_pointer.read(3)
# print(content)
# content=file_pointer.read(3)
# print(content)


#2
# content=file_pointer.read(444444)
# print("1",content)
# content=file_pointer.read(88988)
# print("2",content)   #second content is ignored,prints files only once


#3 for character by character read using for loop
# for char in file_pointer:
#     print(char,end="")

#4 for line by line character reading using for loop
#dont write read the file command/code
#i.e remove the code file_pointer.read()
#directly write
# for line in file_pointer:
#     print(line,end="")

#5 line by line without using for loop
# print(file_pointer.readline())
# print(file_pointer.readline())

#6 to store everylines of file in list
print(file_pointer.readlines())
file_pointer.close()

