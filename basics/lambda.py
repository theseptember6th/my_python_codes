# minus=lambda x,y:x-y
# # above function is equivalent to 
# # def minus(x,y):
# #     return x-y
# print(minus(5,1))



#2
# def a_first(a):
#     return a[1]

# a=[[1,14],[5,6],[4,23]]
# a.sort(key=a_first)
# print(a)

#above is equivalent to
a=[[1,14],[5,6],[4,23]]
a.sort(key=lambda x:x[1])
print(a)