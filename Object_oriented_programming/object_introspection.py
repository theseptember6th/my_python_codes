class Animal:
    var = 5
    def __init__(self, name, species):
        print("from the first base class")
        self.name = name
        self.species = species
        print("from the first base class")
    
    @staticmethod   
    def sound():           
        print("sound by animal")

class Mammal:
    var = 10  # common attribute
    def __init__(self, name, species):
        print("from the second base class")
        self.name = name
        self.species = species
        print("from the second base class")
     
    @staticmethod
    def sound():  
        print("sound by mammal")

class Dog(Animal, Mammal): 
    def __init__(self, name, breed):
        print("from the derived class")
        # Calling the constructors of the base classes
        Animal.__init__(self, name, species="dog")
        Mammal.__init__(self, name, species="dog")
        self.breed = breed

    def sound(self):  # method overriding
        Animal.sound()
        Mammal.sound()  # function from animal and mammal 
        print("Bark!")

derived_object = Dog("tommy", "germanshepherd")

import inspect

print(inspect.isclass(derived_object))  # False, because derived_object is an instance, not a class
print(inspect.ismodule(inspect))  # True, because inspect is a module
print(inspect.isfunction(print))  # True, because print is a function
print(inspect.getmro(Dog))  # Method Resolution Order for the Dog class

inspection = inspect.getmembers(derived_object)  # all members built-in + user-defined stored as tuples in inspection

# to get only methods
methods = inspect.getmembers(derived_object, predicate=inspect.isfunction)
for fun in methods:
    print(fun)

# to get only user-defined methods
def is_user_defined_method(member):
    return inspect.isfunction(member) and member.__module__ == __name__

user_methods = inspect.getmembers(derived_object, predicate=is_user_defined_method)
for fun in user_methods:
    print(fun)
