# exercise 2 - faulty calculator
# 45*3=555, 56+9=77,56/6=4
while(1):
    print('''which operator  do you wanna use
       + for addition
       - for subtraction
       * for multiplication
       / for division
       ^ for power''')
    operator=input()
    print("enter first number")
    num1=int(input())
    print("enter second number")
    num2=int(input())

    if(operator=="*"):
        if((num1==45 and num2==3) or(num1==3 and num2==45)):
            print("555")
        else:
            print(num1*num2)
    elif(operator=="+"):
        if((num1==56 and num2==9)or(num1==9 and num2==56)):
            print("77")
        else:
            print(num1+num2)    
    elif(operator=="/"):
        if((num1==56 and num2==6) or (num1==6 and num2==56)):
            print("4")
        else:
            print(num1/num2)
    elif(operator=="-"):
        print(num1-num2)
    elif(operator=="^"):
        print(num1^num2)
    else:
        print("invalid operator")

    print('''do you want to continue using calculator
          Press Y to continue using
          Press N to exit''')
    x=input()
    x.capitalize()
    if(x=='Y'):
        continue
    elif(x=='N'):
        break 
    else:
        print("invalid character")
        break 




