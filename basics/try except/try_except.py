a=input("enter a number")
b=input("enter second number")
try:
    print("the sum is ",int(a)+int(b))
except Exception as c:
    print(c)

print("program continued even after the error")