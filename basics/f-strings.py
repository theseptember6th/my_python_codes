#1st method
# me="kristal"
# a="this is %s"%me
# print(a)

# #as a tuple
# she="ak"
# a="this is %s %s"%(me,she)
# print(a)

#but better way to do is "2nd METHOD"
# me="kristal"
# she="ak"
# a="this is {1} {0}"
# b=a.format(me,she)
# print(b)
# print(a)



#but best way is f-string
import random
me="kristal"
she="ak"
a=f"this is {me} {she} {random.randint(0,5)}"
print(a)