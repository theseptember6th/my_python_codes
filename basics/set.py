s=set()
print(type(s))
l=[5,6,7,8]
s_from_anotherlist=set(l)
print(type(s_from_anotherlist))
print(s_from_anotherlist)
print(type(s_from_anotherlist))
s_from_list=set([1,2,3,4])
print(s_from_list)
print(type(s_from_list))
s.add(1)
s.add(1)
s.add(2)
s1=s.union({1,2,3})
print(s,s1)
print(len(s1))
print(max(s1))
print(min(s1))
s2=s.intersection({1,2,3})
print(s2)
s3=s.difference({1,2,3})
print(s3)
