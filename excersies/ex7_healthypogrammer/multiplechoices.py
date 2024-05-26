from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]='1'
import pygame,sys,time
pygame.mixer.init()
print("enter 1 to play eye song")
print("enter 2 to play water song")
print("enter 3 to play physical song")
print("enter other integers  to exit")
while 1:
    try:
        choice=int(input("Command: "))
    except Exception as c:
        print(c)    
    if(choice==1):
        pygame.mixer.music.load("eyes.mp3")
        pygame.mixer.music.play()
    elif(choice==2):
        pygame.mixer.music.load("water.mp3")
        pygame.mixer.music.play()
    elif(choice==3):
        pygame.mixer.music.load("physical.mp3")
        pygame.mixer.music.play()
        time.sleep(3) #next execution will be 3 second delayed
        pygame.mixer.music.set_volume(0.1)#this execution is done after 3 sec..volume is down to 10% ie. 0.1
    else:
        print("Exiting the program")
        sys.exit()
   




