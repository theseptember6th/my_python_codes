def kristal():
    x=20
    def shrestha():
        global x
        x=88
    print("before calling shrestha()",x)
    shrestha()
    print("after calling shrestha()",x)

kristal()
print(x)    