#class methods that can change  the value of the class variables 

class kristal:
    age=20
    name="kristal"
    

    @classmethod
    def change_age(cls,newage):  #cls is keyword
        cls.age=newage

object1=kristal()
object1.age=10  #this changes the object's variables values and not of the generic class
print(object1.age)
object1.change_age(18)  #this will change the variable's value of the generic class

object2=kristal()
print(object2.age)
