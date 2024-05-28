# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book

# KristalLibrary = Library(listofbooks, library_name)


#dictionary (books-nameofperson)

# create a main function and run an infinite while loop asking
# users for their input

import sys

class library:
    def __init__(self,listofbooks,library_name):
        self.listofbooks=listofbooks
        self.library_name=library_name
        self.dict={} #dictionary for books-nameofperson to track record

    def display_book(self):
        print("S.N BOOK NAME")
        for i,item in enumerate(self.listofbooks):
            print(f" {i+1}  {item}")

    def lend_book(self, book, user):
        if book in self.listofbooks:
            if book in self.dict.keys():
                print(f"Sorry, {book} is already taken by {self.dict[book]}")
            else:
                self.dict[book] = user
                print(f"Database is updated, you can take the {book} book now")
        else:
            print(f"This {book} book does not exist in our library")

        
                
    def add_book(self,book,user):
        if book in self.listofbooks:
            print(f"this {book} Book is already available in our library")
        else:
            self.listofbooks.append(book)
            print(f"{book} Book is added succesfully")  
            print(f"Thank you {user} for your contribution to our library")  
      
    def return_book(self,book,user):
        if book in self.dict.keys():
            if self.dict[book]==user:
                del self.dict[book]
                print(f"Database is updated,{user} returned book sucessfully")
            else:
                print(f"Error!,You are not {self.dict[book]}, the one who took the book previously")

        else:
            print("This {book} Book is not from our library")    

if __name__ == '__main__':
    Kristal_library=library(['PYTHON','C','C++','HTML','CSS','JS','Mongo DB','EXPRESS JS','REACT JS','NODE JS'],"HAMRO LIBRARY")
    print("\n\tWELCOME TO ONLINE LIBRARY MANAGEMENT SYSTEM")
    print("\n PRESS 1 - display book")
    print(" PRESS 2 - lend book")
    print(" PRESS 3 - add book")
    print(" PRESS 4 - return book")
    print(" PRESS 5 - exit the OLMS")

    while(1):
        choice=int(input("Command- "))
        if choice==1:
            Kristal_library.display_book()

        elif choice==2:
            user_name=input("enter your name: ")
            user_book=input("enter the book you want to lend: ")
            Kristal_library.lend_book(user_book,user_name)

        elif choice==3:
            user_name=input("enter your name: ")
            user_book=user_book=input("enter the book you want to add: ")
            Kristal_library.add_book(user_book,user_name)

        elif choice==4:
            user_name=input("enter your name: ")
            user_book=user_book=input("enter the book you want to return: ")
            Kristal_library.return_book(user_book,user_name)

        elif choice==5:
            print("Exiting the online library management system")
            sys.exit(0)
        
        else:
            print("Warning! please enter the correct integer command ")
            continue



        
