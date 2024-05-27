# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         self.email=f"{lname}{fname}42@gmail.com"
    
#     def printdetails(self):
#         return f"{self.fname},{self.lname},{self.email}"


# object1=Employee("kristal","shrestha")

# print(object1.printdetails())

# object1.fname="Aditi"  #this wont affect the email beacause email was initialized using constructor ..so while fname gets updated email remains the previous one
# print(object1.printdetails())

# #however you could update the email explicitlty aas
# #object1.email=f"{object1.fname}{object1.lname}42@gmail.com"



#you could solve this problem using setter  @property decorator
class Employee:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    
    @property
    def email(self):   #automatically does the changes
        print("property decorator for email attribute is activated each time when email attribute is accessed")
        if(self.fname==None or self.lname==None):
            return "Email is not set. Please set it again using setter"
        else:    
            return f"{self.lname}.{self.fname}@gmail.com"
    
    @email.setter
    def email(self,string):    #email=lastname.firstname@gmail.com
        print("setter of email attribute is activated each time when email attribute is assigned a new value")
        names=string.split("@")[0]  #takes list of lastname and firstname 
        self.lname=names.split(".")[0] #takes last name
        self.fname=names.split(".")[1] #takes first name
    
    @email.deleter
    def email(self):
        print("deleting email using deleter")
        self.fname=None
        self.lname=None
    
    def printdetails(self):
        return f"{self.fname},{self.lname},{self.email}"
    


object1=Employee("kristal","shrestha")

print(object1.printdetails())

object1.fname="Aditi" 
print(object1.printdetails())


#you could also check as
print(object1.email)
#print(object1.email()) #error

#now you cant set email attribute like this in absence of setter
#because property is read only mode
#object1.email=f"{object1.fname}.{object1.lname}@gmail.com"

#for this you need setter
object1.email="shrestha.kristina@gmail.com"   #call to the setter
print(object1.fname,object1.lname,object1.email) #u can see every values are updated



#you could also delete attributes
# del object1.fname#success
# del object1.lname #sucess

#now if i want to delete the email attribute
del object1.email #error because there is no deleter for email ..so we need to create deleter
print(object1.email)


#after deleting you could still set the email
object1.email="bhandari.pranisha@gmail.com"
print(object1.email)