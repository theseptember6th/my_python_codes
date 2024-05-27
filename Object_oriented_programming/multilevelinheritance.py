class Animal:
    var=10
    animal_=20

    def __init__(self,name,species):
        self.name=name
        self.species=species

    def show_details(self):
        print(f"name={self.name}\nspecies={self.species}")    

class Dog(Animal):
    var=30
    dog_=40

    def __init__(self,name,breed):
        self.name=name
        self.breed=breed
    
    def show_details(self):
        print(f"name={self.name}\nbreed={self.breed}")

class Germanshepherd(Dog):
    var=50
    Germanshepherd_=60

    def __init__(self,name,color):
        print("executing constructor of Animal ")
        species=input("enter the species name")
        Animal.__init__(self,name,species)
        print("executing constructor of dog class")
        breed=input("enter the breed name")
        Dog.__init__(self,name,breed)
        print("executing constructor of Germanshepherd")
        self.name=name
        self.color=color

    def show_details(self):
        Animal.show_details(self)
        Dog.show_details(self)
        print(f"name={self.name}\ncolor={self.color}")   


if __name__ == '__main__':
    gs=Germanshepherd("tommy","Red")
    gs.show_details()
