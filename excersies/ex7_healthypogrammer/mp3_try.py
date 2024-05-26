from os import environ
environ["PYGAME_HIDE_SUPPORT_PROMPT"]='1'
import pygame,sys,time
pygame.mixer.init()
pygame.mixer.music.load("physical.mp3")
pygame.mixer.music.play()
input("enter anything + enter to exit")

#make sure you are running code in this folder directory