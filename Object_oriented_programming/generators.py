# first we need to know about iterables,iterator and iteration

# 1 iterables

# iterables are the object that can be placed inside a loop and can return one variable at a time.
# for eg- string,list,tuples,etc

# a="hello"
# for item in a:
#     print(item)

#here a is an iterable

#2  iterators

#iterators are the objects that does iterations on iterables.Meaning it will move character by character

#every iterable has two inbuilt functions __iter__() and __next__()
#__iter__() creates an object for iterables
#__next__() that object moves from one character to another

#3 iteration
#the combination of above two process is known as iteration
#iteration is also a repetition of same command


#Generators
# Generators concept is also very similar as it is used to make an iterator. The only difference comes in the return statement. The generator does not use a return statement. Instead, it uses a yield keyword. Yield functionality is very similar to return as it returns a value to the caller, but the difference is that it also saves the state of the iterator. Meaning that when we use the function again, the yield will resume the value from the place it left off. 

# Generators in Python are created just like the normal functions using the ‘def’ keyword. Generator functions do not run by their name, and they are run when the __next__() function is called. A generator is very helpful in projects relating to memory issues because, like a simple iterator, it does not return all the values at a time; instead, it produces, series of values over time. So a generator is generally used when we want to iterate over a series of values but do not want to store them completely in memory. 


def gen(x):          #generator function
    for i in x:
        yield i

string="kristal" #or any iterable objects lst=[1,2,3,4]
iterable_object=iter(string) #now iterable_object of string is created
print(iterable_object.__next__()) #one character is executed and holds the state
print("hi")
print(iterable_object.__next__())#another character is executed and so on

# The most significant advantage of generators is that the memory is saved as the items are produced when required.

print(gen(string))


#more examples 
#factorial and fibonacci using generator

def factorial_generator(): 
    n=0
    fact=1
    while 1:
        yield fact
        n+=1
        fact*=n

def fibonacci_generator():
    a,b=0,1
    while 1:
        yield a
        a=b
        b=a+b

fact_gen=factorial_generator() #another way to initialize the generators
print(fact_gen.__next__())
print(fact_gen.__next__)

fibonacci_gen=fibonacci_generator()
print(fibonacci_gen.__next__())
print(fibonacci_gen.__next__())


