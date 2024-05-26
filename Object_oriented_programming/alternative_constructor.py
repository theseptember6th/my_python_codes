class Kristal:
    age=20
    name="kristal"

    def __init__(self,age,name,college):
        self.age=age
        self.name=name
        self.college=college

    def printdetails(self):
        print(f"age={self.age}\nname={self.name}\ncollege={self.college}")


    # @classmethod
    # def from_str(cls,string):
    #     lst=string.split("-")    #returns a list of string   variables as members of list seperated by hyphon(-)  
    #     return cls(lst[0],lst[1],lst[2]) #goes to constructor
    

    #15 no code can also be done in one line as follows
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    # string.split("-") returns a list of string   variables as members of list seperated by hyphon(-)
    # * make sure that members of list are seperate parameters
    


object1=Kristal.from_str("89-albert_einstein-Cambridge_University") #initializing object1 variable by this way
object1.printdetails()
print(Kristal.age)




#the use of this is when we have a text file
#where datas are in format
#age-name-college
#then you can directly create objects with this method such that it will be easy to understand and use