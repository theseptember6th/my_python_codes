#*args is used when we have to take multiple parameters
#* is compulsory ,and you can name anything
# def funargs(normal,*king):
#     #print(king[0])
#     print(type(king))
#     for i in king:
#         print(i)
#     print(normal)

# lst=["kristal","aditi","pranisha","biraj"]
# funargs("hello",*lst)
# funargs("khanal","shrestha")
# funargs(1)


#**kwargs

def funargs(normal,*args,**kwargs):
    print(args[0])
    print(type(args))
    print(type(kwargs))
    for i in args:
        print(i)
    
    for key,value in kwargs.items():
        print(f"{key} is {value}")


lst=["kristal","aditi","pranisha","biraj"]
dict={"kristal":"king","aditi":"queen","pranisha":"princess","biraj":"prince"}
funargs(1,*lst,**dict)