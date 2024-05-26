#creating copy of function

# def function1():
#     print("hello, I am kristal")
# func2=function1
# print("before deleting funtion1")
# func2() 
# del function1   
# print("after deleting function 1")
# func2()


#returning function

# def function1(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
    
# a=function1(1)
# print(a) 

#function as argument

# def executor(func):
#     func("this is the copy of print function")
# executor(print)

#concept of decorators
# Python decorators are a powerful and versatile tool that allow you to modify the behavior of functions and methods. They are a way to extend the functionality of a function or method without modifying its source code.

# A decorator is a function that takes another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a "decorated" function.

#example 1

# def greet(fx):
#     def mfx(): #modified function==mfx
#         print("good morning")
#         fx()
#         print("thank you for using this function")
#     return mfx    
        
# @greet   #this is important otherwise wont work
# def hello():
#     print("hello my name is kristal shrestha")
# hello() 
#modifying hello function without changing its source code
#hello=greet(hello)
#hello is mfx now

# now for a parameter function
def greet(fx):
    def mfx(*args): #modified function==mfx
        print("good morning")
        fx(*args)
        print("thank you for using this function")
    return mfx  
def add(a,b):
    return a+b
print(add(1,2))
#example 2

# def dec1(func1):
#     def nowexec():
#         print("Executing row")
#         func1()
#         print("Excecuted")
#     return nowexec
# @dec1
# def who_is_kristal():
#     print("kristal is a good boy")

# #who_is_kristal=dec1(who_is_kristal)
# #37 line == 41 line
# who_is_kristal()






