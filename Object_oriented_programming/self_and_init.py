#self
# class kristal:
#     age=20
#     name="kristal"
#     def printdetails(self):  #self is like a this pointer of C++,it takes the object that invoked this function
#         return f"Name is {self.name}.Age is{self.age}"

# object1=kristal()
# object1.name="shrestha"
# object1.age=18
# result=object1.printdetails()
# print(result)
# print(object1.printdetails())

# #if self was removed,it will give error

# object2=kristal()
# print(object2.printdetails())


#__init__  is like a constructor

class Kristal:  #class name should have first letter capital
    age=20
    name="kristal"
    def printdetails(self):
        return f"Name is {self.name}.Age is{self.age}"


    def __init__(self,name,age,college):   #equivalent to parameterized constructor
        self.name=name
        self.age=age
        self.college=college

object3=Kristal("albert einstein",89,"Cambridge University")
result=object3.printdetails()        
print(result)

#object4=kristal()  #this will give error because there is paremeterized constructor
