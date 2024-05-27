# The super() keyword in Python is used to refer to the parent class. 

#super() in single inheritance
# class ParentClass:
#     def parent_method(self):
#         print("This is the parent method.")

# class ChildClass(ParentClass):
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()


#multiple inheritance
# example 1
# class ParentClass1:
#     def parent_method(self):
#         print("This is the parent method of ParentClass1.")

# class ParentClass2:
#     def parent_method(self):
#         print("This is the parent method of ParentClass2.")

# class ChildClass(ParentClass1, ParentClass2): #priority based
#     def child_method(self):
#         print("This is the child method.")
#         super().parent_method()

# child_object = ChildClass()
# child_object.child_method()

#example 2
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        super().__init__()
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
