#to use abstract class ,you need to import
from abc import ABC,abstractmethod
class Polygon(ABC):
    @abstractmethod     
    def area():            #similar to  pure virtual function of C++
        return 0            #so this method must be override otherwise,you cant created derived object and cant create object of the abstract class
                           
class Rectangle(Polygon):
    length=10
    breadth=40  
    def area(self,length,breadth):   #if this not created ,it will generate error
        return self.length*self.breadth
    
object2=Polygon()
object1=Rectangle()
print(f"the area is {object1.area(20,30)}")

