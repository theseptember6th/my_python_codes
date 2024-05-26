def funargs(normal,*king):
    print(king[0])
    print(type(king))
    for i in king:
        print(i)

lst=["kristal","aditi","pranisha","biraj"]
funargs("hello",*lst)
funargs("khanal","shrestha")
funargs(1)