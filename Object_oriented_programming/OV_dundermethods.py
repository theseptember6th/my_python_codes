# Methods starting with a double underscore ( __ ) and ending with a double underscore ( __ ) represent dunder methods.
# unlike C++ here we cant use operator + ....we have to use name of the dunder function to overload it and use it to do anything
# Check https://docs.python.org/2/library/operator.html to explore more about operator overloading.
class kristal:
    age=20
    name="kristal"
    
    #dunder method
    def __init__(self,age,name):
        self.age=age
        self.name=name

    #dunder method 
    def __add__(self,other):  #operator overloading of binary operator +, we cant write +,isntead you have to write __add__                         
        return self.age+other.age
    
    #dunder method 
    def __sub__(self,other):    #operator overloading of  binary operator -
        return self.age-other.age

    #dunder method 
    def __neg__(self):       #operator overloading of unary operator -
        return self.age-1   
    
    #inbuilt methods
    def __str__(self):
        return f"The name is {self.name}.The age is {self.age}"
    
    def __repr__(self):
        return f"kristal('{self.name}',{self.age})"
    
object1=kristal(40,"Aditi")
object2=kristal(50,"kristal")
print(object1+object2)
print(object1-object2)
print(-object2)

#there are two special functions 
#__str__ and __repr__ functions
#used when we do sth like this 
#print(object1) 
#giving the complete description of the object
#str has more priority than repr
#str ==written for end user
#repr == written for developer

print(object1)
print(str(object1))
print(repr(object2))



