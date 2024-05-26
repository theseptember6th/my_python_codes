# list1=[1,2,3,4]
# sum=0
# for i in list1:
#     sum=sum+i
# print(sum)

#you can do this in one line using reduce function
# We can’t directly use reduce like map or filter function. We have to import it first.
from functools import reduce
list1=[1,2,3,4]
sum=reduce(lambda x,y:x+y,list1)
print(sum)
