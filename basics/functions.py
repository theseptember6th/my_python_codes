# a=5
# b=10
# c=sum([a,b])
# print(c)
def function1(a,b):
    print("the sum is ",a+b)
def function2(a,b):
    """ this is the function to do average of two numbers"""
    average=(a+b)/2
    print("the average is ",average)
    return average
function1(3,4)
average=function2(3,4)
print(average)
print(function2.__doc__)