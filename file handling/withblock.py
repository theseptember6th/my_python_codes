with open("kristal.txt") as file_pointer:
    a=file_pointer.read(4)
    print(a)

file_pointer=open("kristal.txt")
print(file_pointer.read())
file_pointer.close()