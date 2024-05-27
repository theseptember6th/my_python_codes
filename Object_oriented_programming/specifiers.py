class Kristal:
    public = 10  # nothing at first is public
    _protected = 20  # _ at first in naming of variables is protected
    __private = 30  # __ at first in naming of variables is private

    def publicmethod(self):
        print("I am a public method")

    def _protectmethod(self):  # protected method
        print("I am a protected method")

    def __privatemethod(self):  # private method
        print("I am a private method")

    # Provide a way to access private methods
    def access_private_method(self):
        self.__privatemethod()


class Shrestha(Kristal):
    def function1_(self):
        _protected = 100  # base class value didn't change
        print(self._protected)  # Accessing protected member
        # __private = 200  # This creates a new local variable, not accessible outside
        # print(self.__private)  # This will raise an error because __private is name mangled
        print(self._Kristal__private)  # Accessing the private variable through name mangling
        self._protectmethod()  # Accessing the protected method
        self.access_private_method()  # Accessing the private method through a public method


class Random:
    pass


if __name__ == '__main__':
    # by child
    object1 = Shrestha()
    print(object1.public)
    print(object1._protected)
    # print(object1.__private)   # error
    
    object1.publicmethod()
    object1._protectmethod()
    # object1.__privatemethod()  # error
    object1.function1_()
    
    # by any random class
    object2 = Random()
    # print(object2.public)            # all error
    # print(object2._protected)
    # print(object2.__private)

    # object2.publicmethod()
    # object2._protectmethod()
    # object2.__privatemethod()
