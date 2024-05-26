"""Snake water gun game is a game which requires two players both have to select something from snake or water or gun. snake wins over water , gun win over snake and water wins over gun. ultimately the player with maximum points wins the game."""

import random
lst=["snake","water","gun"]
count=1
player,bot=0,0 # to count no. of wins out of 9
while(count<=9):
    computer=random.choice(lst)
    guess=input("write snake or water or gun: ") #write string

    if((computer=="snake" and guess=="snake")or(computer=="gun" and guess=="gun")or(computer=="water" and guess=="water") ):
       print("bot choosed ",computer)
       print("you choosed ",guess)
       print("Draw in round ",count)

    elif((computer=="snake" and guess=="water")or(computer=="gun" and guess=="snake")or(computer=="water" and guess=="gun")): 
        print("bot choosed ",computer)
        print("you choosed ",guess) 
        print("bot won round ",count)
        bot+=1
    
    elif((guess=="snake" and computer=="water")or(guess=="gun" and computer=="snake")or(guess=="water" and computer=="gun")): 
        print("bot choosed ",computer)
        print("you choosed ",guess)  
        print("You won round ",count)
        player+=1

    else:
        print("bot choosed ",computer)
        print("you choosed ",guess) 
        print(" your invalid choice,bot won ",count,"round")

    count+=1
    print("bot: ",bot,"v/s\tyou: ",player)

if(bot>player):
    print("You lose")
elif(bot<player):
    print("Congratulations!,you won!")
else:
    print("ITS A DRAW")
    
  