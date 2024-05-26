str1="kristal shrestha"
str2="kristalshrestha"
print(str1)
print(str1[0])
print(str1[0:3])
print(len(str1))
print(str1[0:16])
#print(str1[77]) #error
print(str1[0:77]) #no error
print(str1[0:6:2]) #takes string from 0 to 6 but with a gap of 2 counting current string as well
print(str1[0:]) #starts from 0 to last index of string
print(str1[:5]) #starts from 0 to 5 of string
print(str1[::])#starts from 0 to last with gap of 1
print(str1[::2])#starts from 0 to last with gap of 2
print(str1[::46958695])#starts from 0 to last with gap of that length it will print first character only
print(str1[-1:0])
print(str1[-4:0])
print(str1[-4:-2])
print(str1[12:14])
print(str1[::-1])
print(str1[::-2])

#string functions

print(str1.isalnum())  #checking for alpha numeric
print(str2.isalnum()) 
print(str1.isalpha())
print(str2.isalpha())
print(str1.isdigit())
print(str2.isdigit())
print(str1.endswith("shrestha"))
print(str2.endswith("shrestha"))
print(str1.endswith("tha"))
print(str2.endswith("tha"))
print(str1.endswith("shristha"))
print(str2.endswith("shristha"))
print(str1.count("a"))  #how many a are there in str1
print(str1.capitalize()) #capitalizes first letter
print(str1.find("tal")) #gives me location of the given argument if present in string
print(str1.lower()) #string in lowercase
print(str1.upper()) #string in uppercase
print(str1.replace("tal","ti"))

