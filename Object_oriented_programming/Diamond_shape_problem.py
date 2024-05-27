#unlike C++ we dont need virtual object or functioon
#python solves it by just prioritizing the one that is closer to it while inhereting

class A:
    def print(self):
        print("I am from the class A")
class B(A):
    def print(self):
        print("I am from the class B")
class C(A):
     def print(self):
        print("I am from the class B")
class D(B,C):
    pass

d=D()
d.print() #prints B's because it is the closest