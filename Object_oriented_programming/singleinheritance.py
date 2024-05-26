class Animal:
    def __init__(self,name,species):#requires object to call
        print("from the base class")
        self.name=name
        self.species=species
        print("from the base class")

    def sound(self): #requires object to call
        print("sound by animal")
    
   
    def printdetails(self):
        print(f"name={self.name},species={self.species}")

    
class Dog(Animal): #inherited from animal
    def __init__(self,name,breed,species):
        print("from the derived class")
        self.name=name
        self.breed=breed
        self.species=species  #variable from parent

    def sound(self):             #method overriding
        Animal.sound(self)        #function from animal through class
        print("Bark!")
    
    
    def printdetails(self):
        Animal.printdetails(self)
        print(f"name={self.name},species={self.species},breed={self.breed}")

derived_object=Dog("tommy","germanshepherd","dog")
#derived_object1=Dog("doggy","bulldog") #error unmatched derived constructor
derived_object.printdetails()
derived_object.sound()
   
