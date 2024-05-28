def searcher():
    print("subroutine first execution is done here using next() ,only once ")
    book="Consider This as a very large data file where you have to search .Its meaningless if you have to again open the book and again use the same resources to open the book and waiting you for longer period of time. SO what subroutine do is it saves all the datas/files/books this in a memory and helps execution faster"
    import time
    time.sleep(5)  #representing a heavy task that takes 5 seconds to execute

#the above code will be executed only once
   
    while 1:
        time.sleep(2)  # to see differences of two send otherwise it is seen in an instant and we might get a bit confused
        print("after that the code of inside  while loop is runned everytime we use send() ")
        text=(yield) #this line is  very very important 
        if text in book:
            print(f"{text} is present in the book")
        else:
            print(f"{text} is not present in the book")


search=searcher()  #initializing 
next(search)   #starts coroutine first execution
search.send("subroutine")
search.send("kristal")
string=input("enter the word you want to search ")
search.send(string)
search.close()
