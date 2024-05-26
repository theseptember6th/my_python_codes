num1=200
count=1
guess=9
print("\t\tYou will have 9 guesses\n")
while(count<=9):
    print("guess the number")
    guess_num=int(input())
    if(guess_num>num1):
        guess-=1
        print("you have ",guess,"guess left")
        print("your guess number is greater than lottery number,so decrease the value")
    elif(guess_num<num1):
        guess-=1
        print("you have ",guess,"guess left")
        print("your guess number is less than lottery, so increase the value")
    else:
        print("you have correctly guessed the number ",num1)
        print("you guessed in ",count," attempt")
        break
    count+=1
if(guess_num!=num1):
    print("\t\tno of guesses has reached its limit,please try again")    