#  The exception is an error that halts the program's normal functioning and displays an error onto the screen. 
# raise keyword, on the contrary, is to raise an exception.
#if test_condition:
#raise EXCEPTION_CLASS_NAME

#  A few of these exceptions include:

# KeyError: Raised when a mapping key is not found in the set of existing keys.
# ValueError: Raised when a function receives an argument with the right type but an inappropriate value.
# EOFError (End Of File Error): Raised when the input() function hits an end-of-file condition without reading any data.
# ImportError: Raised when the import statement has trouble trying to load a module.
# NameError: Raised when a local or global name is not found.
# ZeroDivisionError: Raised when the second argument of a division is zero.


#Example 1
# Suppose we have made a program in which we want a number that is greater than 10. Now the user is giving the input (x),  5. So in such a case, we can raise ValueError, returning an error to the user that the input is wrong. By doing this, we can save the program running time and prevent the program from storing the wrong input.

# x=input("enter number greater than 10")
# if int(x)<=10:
#     raise ValueError("value less than 10")
# print("this code will only run if there is no raise, if there is raise ,program terminates without printing this statemenet")


#Example 2

# name=input("Enter your name ")
# salary=input("Enter your salary")
# if(int(salary)==0):
#     raise ZeroDivisionError("salary is 0 so stopping the error")
# #this zeroDivision error is not appropriate here,but i want to show that we can manually raise exception as we want.
# #if this error raised line 33 wont  be executed as program will stop
# if(name.isnumeric()):
#     raise Exception("Numbers cannot be entered while naming")
# #general raising exception

# print("Program executed successfully without raise")





#Example 3

#A program that takes string only and block a certain username

name=input("Enter your Name: ")
try:
    print(a)  #to raise an exception forcefully as a is not a predfined variable
except Exception as c:
    print(c)
    if name=="kristal":
        raise ValueError("Kristal username is blocked,please try another one")
        #program ends here if there is raise

print("system runned sucessfully without raise")