class kristal():
    public=10      # nothing at first is public
    _protected=20   # _ at first in naming of variables is protected
    __private=30    # __ at first in naming of variables is private

    def publicmethod(self):
       print("I am public method")

    def _protectmethod(self):  #protected attribute
       print("I am protected method")

    def __privatemethod(self):  #private attribute
        print("I am private method")


class shrestha(kristal):
    pass

class random():
    pass
if __name__ == '__main__':
    #by child
    object1=shrestha()
    print(object1.public)
    print(object1._protected)
    # print(object1.__private)   #error
    
    object1.publicmethod()
    object1._protectmethod()
    # object1.__privatemethod() #error
    
    # by any random class
    object2=random()
    # print(object2.public)            #all error
    # print(object2._protected)
    # print(object2.__private)

    # object2.publicmethod()
    # object2._protectmethod()
    # object2.__privatemethod()


