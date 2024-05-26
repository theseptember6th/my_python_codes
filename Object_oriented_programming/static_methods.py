# Static methods are often used to create utility functions that don't need access to instance data.
#  The method can be called on the class itself, without the need to create an instance of the class.
class kristal:
    age=20
    name="kristal"

    @staticmethod
    def printgood(string):
        print(f"this is good {string}")
        age=30

object1=kristal()
kristal.printgood("food")
print(kristal.age)
object1.printgood("planet")
print(object1.age)


#here the age value wont be changed because the age variable inside static method localvariable and not class or object variable also because there is no use of self,and cls parameters to acess class/object's age