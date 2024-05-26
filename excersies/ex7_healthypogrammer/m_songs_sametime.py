from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]="1"
import pygame,sys,time
pygame.mixer.init()

effect1=pygame.mixer.Sound("eyes.mp3")
effect2=pygame.mixer.Sound("water.mp3")
effect3=pygame.mixer.Sound("physical.mp3")

print("1 = effect1")
print("2 = effect2")
print("3 = effect3")
print("4 = special combo effect")
# print("5 = pause music")  #sound doesnot support pause unpause
# print("6 = unpause music")
print("7 = stop music")
print("other integers = exit")

while(1):
    try:
        choice=int(input("Command: "))
    except Exception as c:
        print("please try again, non-integer command")
    
    if(choice==1):
        effect1.play()
    elif(choice==2):
        effect2.play()
    elif(choice==3):
        effect3.play()
    elif(choice==4):
        print("effect1.play()")
        effect1.play()
        time.sleep(3)
        print("effect1.set_volume(0.1)")
        effect1.set_volume(0.1)
        print("effect2.play()")
        effect2.play()
        time.sleep(3)
        print("effect2.set_volume(0.3)")
        effect2.set_volume(0.3)
        time.sleep(3)
        print("effect3.play")
        effect3.play()
        print("effect3.set_volume(0.8)")
        effect3.set_volume(0.8)
    # elif(choice==5):
    #     try:
    #         a=int(input("want to pause 1,2 or 3 "))
    #     except Exception as c:
    #         print("please enter valid integer")    
    #     if(a==1):
    #         effect1.pause() 
    #     elif(a==2):
    #         effect2.pause() 
    #     elif(a==3):
    #         effect3.pause()
    #     else:
    #         print("invalid command")
    # elif(choice==6):
    #     try:
    #         a=int(input("want to unpause 1,2 or 3 "))
    #     except Exception as c:
    #         print("please enter valid integer")    
    #     if(a==1):
    #         effect1.unpause() 
    #     elif(a==2):
    #         effect2.unpause() 
    #     elif(a==3):
    #         effect3.unpause()
    #     else:
    #         print("invalid command")
    elif(choice==7):
          effect1.stop()               
          effect2.stop()               
          effect3.stop()               


            
    else:
        print("Exiting the program")            
        sys.exit()