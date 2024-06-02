# The task you have to perform is “Pickling Iris.” For this, Check the UC Irvine Machine Learning Repository site to get the dataset. You can search the Iris dataset through their searchable interface. Follow the following steps to download the dataset:

# Go to https://archive.ics.uci.edu/ml/index.php
# On Most Popular Data Sets, you will see the name “Iris.”
# Open the Iris dataset.
# Click on the Data folder. A new tab will open, which contains some files.
# Click on the Iris. data file to download the text file.
# After saving Iris. data file, parse it using the split() function or using a new line approach. The method of parsing is up to you.

# The main task is to get the list of lists that you will pickle. And after creating the pickle, write a code to read it. For downloading the Iris dataset, use the request module


import requests
import pickle

# data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text  #converting response to text format
# #print(data)  #for conformation if it is converted to text

# #converting data to list
# list1=data.split("\n")
# #print(list1)  #just for conformation if it is converted to list

# #converting to list of list
# list2=[item.split(",") for item in list1 if len(item)!=0]
# #creating list from list1 seperated by "," ,and not taking backslashes "\n"
# print(list2) #just for conformation

# with open("myiris.pkl","wb") as file_pointer:
#     pickle.dump(list2,file_pointer)

# #now my list2 is pickled in file_pointer i.e myiris.pkl
# #Part 1 Completed


#now reading by unpickling

with open("myiris.pkl","rb") as f:
    lst=pickle.load(f) #back to my original format
    print(lst)
    print(type(lst))

