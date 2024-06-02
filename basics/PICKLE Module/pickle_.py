import pickle
#pickling process

# py_dict={"name":"kristal","salary":200000} #dictionary to be pickled
# myfile=open("KRISTAL.pkl","wb") #pickling pydict to myfile
# pickle.dump(py_dict,myfile)
# myfile.close()

#unpicking

myfile=open("KRISTAL.pkl","rb")
py_dict=pickle.load(myfile)  #unpickling myfile and saving to py_dict object
#this py_dict object will be same as the pickled object stored in myfile
print(py_dict) #printing the content
print(type(py_dict))#confirmation for line 13
myfile.close()

