#is-> identity operator->reference equality->two references refers to same object
#== ->Equality operatior ->value Equality ->two objects having same value



a=[1,2,3]
b=a  # assigning variables means they are pointing to same reference
#changing b will also change a
b[0]=5
print(b,a)
print(b==a) #true
print(b is a) #true

c=a[:] #creates copy of a
print(c==a) #true
print(c is a)#false

d=[1,2,3]
e=[1,2,3]
print(d==e) #true
print(d is e) #fasle
