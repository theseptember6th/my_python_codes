# It's important to note that, in case of multiple inheritance, Python follows a method resolution order (MRO) to resolve conflicts between methods or attributes from different parent classes. The MRO determines the order in which parent classes are searched for attributes and methods.

class Animal:
    var=5  #common attribute
    def __init__(self,name,species):
        print("from the first base class")
        self.name=name
        self.name=species
        print("from the first base class")
    
    @staticmethod   #your choice to decorate staticmethod or not in both case works as we are not using instances,class
    def sound():            #common method-
        print("sound by animal")

class Mammal:
    var=10 #common attribute
    def __init__(self,name,species):
        print("from the second base class")
        self.name=name
        self.species=species
        print("from the second base class")
     
    @staticmethod
    def sound():  #common method
        print("sound by mammal")


    
class Dog(Animal,Mammal): #inherited from animal
    def __init__(self,name,breed):
        print("from the derived class")
        self.name=name
        self.breed=breed
        self.species="dog"  #variable from parent

    def sound(self):             #method overriding
        Animal.sound()
        Mammal.sound()      #function from animal and mammal 
        print("Bark!")

derived_object=Dog("tommy","germanshepherd") #only derived class constructor gets invoked  #no constructor invokation order
derived_object.sound()
print(derived_object.var) #prints var of Animal as it is inherited first 

#no ambiguity
