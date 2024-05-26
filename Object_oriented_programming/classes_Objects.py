class kristal:
    age=20       #you can put values in variables,,unlike C++
    name="kristal"
object1=kristal()  #syntax similar as function
print(object1.name)
object1.name="shrestha"
print(object1.name)
object1.college="lalitpur engineering college"   #can create new variables that is not present in class
print(object1.college)
print(object1.__dict__)