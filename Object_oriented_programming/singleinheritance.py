class Animal:
    def __init__(self,name,species):
        print("from the base class")
        self.name=name
        self.species=species
        print("from the base class")

    def sound():
        print("sound by animal")
    
class Dog(Animal): #inherited from animal
    def __init__(self,name,breed):
        print("from the derived class")
        self.name=name
        self.breed=breed
        self.species="dog"  #variable from parent

    def sound(self):             #method overriding
        Animal.sound()        #function from animal through class
        print("Bark!")

derived_object=Dog("tommy","germanshepherd")
derived_object.sound()        
