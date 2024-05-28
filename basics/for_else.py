# When we use else with for loop, the compiler will only go into the else block of code when two conditions are satisfied:

# The loop is normally executed without any error.
# We are trying to find an item that is not present inside the list or data structure on which we are implementing our loop.

# Except for these conditions, the program will ignore the else part of the program. For example, if we are just partially executing the loop using a break statement, then the else part will not execute. So, a break statement is a must if we do not want our compiler to execute the else part of the code.


Persons=["kristal","Aditi","Biraj","Pranisha"]
choice=input("enter the name of person to search: ")
for name in Persons:
    if(name==choice):
        print("Person found")
        break
else:
    print("Person not found")
    print("for loop executed succesfully")        