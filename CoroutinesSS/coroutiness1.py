def myfunc(): #coroutine
    print("this line is executed only once by next()")
    while 1:
        print("after the first execution,from line 5 will be executed using send()")
        value=(yield)
        print(value)

coroutine=myfunc()  #same as generator
next(coroutine)  # only line 2 gets executed
coroutine.send("kristal")
coroutine.send("shrestha")
coroutine.close() # to get out of while loop + deactivate myfunc()