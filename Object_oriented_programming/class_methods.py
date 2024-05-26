#class methods is the methods that can be used by objects and that can change  the value of the class variables 

class kristal:
    age=20
    name="kristal"
    

    @classmethod
    def change_age(cls,newage):  #cls is keyword for class
        cls.age=newage

object1=kristal()
object1.age=10  #this changes the object's variables values and not of the generic class
print(object1.age)
object1.change_age(18)  #this will change the variable's value of the generic class by object

object2=kristal()
print(object2.age)


#however you can directly change value of class using class
kristal.age=30   
print(object2.age)
