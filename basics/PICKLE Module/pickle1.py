import pickle
import pprint

data1=[{'a':'A','b':2,'C':3.0}]
print("BEFORE: ",)
pprint.pprint(data1)
data1_string=pickle.dumps(data1) #pickling data1 and storing in data1_string
print("dumps ",)
pprint.pprint(data1_string)
data2=pickle.loads(data1_string)#unpickling data1_string and storing in data2
print("AFTER: ",)
pprint.pprint(data2)
print("SAME: ",(data1 is data2)) #they arenot same because they arenot same object in memory
print("EQUAL: ",(data1==data2)) #but they are equal in content
