file_pointer=open("kristal.txt","r+")
print(file_pointer.read())
file_pointer.write("\nkristal is a hero") #it appends the file
file_pointer.close()