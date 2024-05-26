# numbers=["3","4","1"]
# for i in range(len(numbers)):
#     numbers[i]=int(numbers[i])
# numbers[2]=numbers[2] + 1
# print(numbers[2])   


#you can do this in shortcut way also 
#with out using for loop
#using map function
# Map function takes two arguments. It takes a function name and a list and it automatically applies that function on all the list items and returns an object. We don’t have to make a for loop and pass those list items through it one by one. Also with the help of this function, code becomes extremely small.
# numbers=["3","4","1"]
# print(map(int,numbers))
# numbers=list(map(int,numbers))
# numbers[2]=numbers[2]+1
# print(numbers[2])



#more examples  create list of squares
# def square(n):
#     return n*n

# numbers=[1,2,4,5,7]
# sq=list(map(square,numbers))
# print(sq)


#or you can use lambda inside parameter too

# numbers=[1,2,4,5,7]
# sq=list(map(lambda x:x*x,numbers))
# print(sq)



#You can also pass list through multiple functions with the help of map function.
def square(x):
    return x*x
def cube(x):
    return x*x*x

fun=[square,cube]

for i in range(5):
    val=list(map(lambda x:x(i),fun))
    print(val)