"""create a dictionary and take input from the user and return the meaning of the word from
the dictionary"""

dictionary={"hello":"https://en.wikipedia.org/wiki/Hello",
            "namaste":"https://en.wikipedia.org/wiki/Namaste",
            "bye":"https://en.wikipedia.org/wiki/Namaste",
            "hi":"https://en.wikipedia.org/wiki/HI"}
print("enter the word you want to search in dictionary")
x=input()
#print(dictionary[x])
print("you can get the required meaning from ",dictionary.get(x))            

