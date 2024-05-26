# Exercise#7 Healthy Programmer
# Assume that a programmer works at the office from 9am-5 pm. We have to take care of his health and remind him three things,

# To drink a total of 3.5-liter water after some time interval between 9-5 pm.
# To do eye exercise after every 30 minutes.
# To perform physical activity after every 45 minutes.
# Instructions:
# The task is to create a program that plays mp3 audio until the programmer enters the input which implies that he has done the task.

# For Water, the user should enter “Drank”
# For Eye Exercise, the user should enter “EyDone”
# For Physical Exercise, the user should enter “ExDone”
# After the user enters the input, a file should be created for every task separately, which contains the details about the time when the user performed a certain task.

# Challenge:
# You will have to manage the clashes between the reminders such that no two reminders play at the same time.
# Use pygame module to play audio.


#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]='1'
import pygame,sys,time,datetime

def music_(music_file,message):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play()
    while(1):
        user_input=input()
        if(user_input==message):
            pygame.mixer.music.stop()
            break

def log_record(message):
    with open("log.txt","a") as file_pointer:
        file_pointer.write(f"{message} at {datetime.datetime.now()}\n")
    print("written your record succesfully")




if __name__== '__main__':
    pygame.mixer.init()
    water_drinking_time=time.time()
    eyes_relaxing_time=time.time()
    physical_activity_time=time.time()
    water_drinking_gap=4 #4 seconds
    eyes_relaxing_gap=8  #8 seconds
    physical_activity_gap=12 #12 seconds
    print("WELCOME TO HEATH REMINDER FOR PROGRAMMERS")
    try:
        while(1):
            if(time.time()-water_drinking_time >= water_drinking_gap):
                print("TIME TO DRINK WATER")
                print("Enter 'Drank' to stop the Reminder ")
                music_("water.mp3",'Drank')
                water_drinking_time=time.time()
                log_record("I drank the water at ")

            if(time.time()-eyes_relaxing_time >= eyes_relaxing_gap):
                print("TIME TO RELAX YOUR EYES")
                print("Enter 'Eydone' to stop the Reminder ")
                music_("eyes.mp3",'Eydone')
                eyes_relaxing_time=time.time()
                log_record("I relaxed my eyes at ")

            if(time.time()-physical_activity_time >= physical_activity_gap):
                print("TIME TO DO SOME EXERCISE")
                print("Enter 'ExDone' to stop the Reminder ")
                music_("physical.mp3",'ExDone')
                physical_activity_time=time.time()
                log_record("I did physical exercise at ")  


            time.sleep(1)     #so my cpu can rest for 1 second every time     
    except KeyboardInterrupt:
        print("keyboard interrupts")
        sys.exit(0)  #normal Termination ,terminated after sucessful completion

    except Exception as c:
        print("an unknown error occured")
        sys.exit(1)     #abnormal Termination,termination due to error







