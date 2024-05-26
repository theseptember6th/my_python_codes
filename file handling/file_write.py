# file_pointer=open("kristal.txt","w")
# file_pointer.write("kristal is a good boy")
# file_pointer.close()

file_pointer=open("kristal.txt","w")
a=file_pointer.write("\nkristal is a hardworker\n")
file_pointer.write("kristal is a hardworker")
print(a)
file_pointer.close()


