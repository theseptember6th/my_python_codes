# Health Management System
# 3 clients - kristal, Aditi and pranisha
# Total 6 files
# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Write a function that takes the user input of the client's name. After the client's name is entered, A message should display "What you want to log. Diet or Exercise"
# Use function

# def getdate():
#     import datetime
#     return datetime.datetime.now()

# The purpose of this function is to give time with every record of food or exercise added in the file.
# Write a function to retrieve exercise or food file records for any client.

import datetime

def getdate():
    return datetime.datetime.now()

def log(person_log):
    if(person_log==1):
        f_e=int(input("PRESS 1 for food\n  Press 2 for exercise "))
        if(f_e==1):
            value=input("enter the food you ate") 
            with open("aditi-food.txt","a")as aditi:
                aditi.write(str([str(getdate())])+": "+value+"\n") #concatenating using +    
                print("written sucessfully")
        elif(f_e==2):
            value=input("enter the exercise you done") 
            with open("aditi-exercise.txt","a")as aditi:
                aditi.write(str([str(getdate())])+": "+value+"\n")   
                print("written sucessfully")
        else:
            print("invalid number")


    elif(person_log==2):
        f_e=int(input("PRESS 1 for food\nPress 2 for exercise "))
        if(f_e==1):
            value=input("enter the food you ate   ") 
            with open("pranisha-food.txt","a")as pranisha:
                pranisha.write((str(getdate()))+": "+value+"\n") #concatenating using +    
                print("written sucessfully")
        elif(f_e==2):
            value=input("enter the exercise you done") 
            with open("pranisha-exercise.txt","a")as pranisha:
                aditi.write(str(getdate())+": "+value+"\n")  
                print("written sucessfully")
        else:
            print("invalid number")  

    if(person_log==3):
        f_e=int(input("PRESS 1 for input food-data\n  Press 2 for input exercise-data "))
        if(f_e==1):
            value=input("enter the food you ate") 
            with open("kristal-food.txt","a")as kristal:
                aditi.write(str(getdate())+": "+value+"\n") 
                print("written sucessfully")
        elif(f_e==2):
            value=input("enter the exercise you done") 
            with open("kristal-exercise.txt","a")as kristal:
                aditi.write(str(getdate())+": "+value+"\n") 
                print("written sucessfully")
        else:
            print("invalid number")

    else:
        print("invalid number")


def retrieve(person_retrieve):
    if(person_retrieve==1):
        f_e=int(input("PRESS 1 to get food-log\n  Press 2 to get exercise-log "))
        if(f_e==1): 
            with open("aditi-food.txt")as aditi: #default opens in read mode
                for i in aditi:
                    print(i,end="")  #char by char reading  
                 
                
        elif(f_e==2):
            with open("aditi-exercise.txt")as aditi:
                for i in aditi:
                    print(i,end="")
        else:
            print("invalid number")


    elif(person_retrieve==2):
        f_e=int(input("PRESS 1 to get food-log\n  Press 2 to get exercise-log "))
        if(f_e==1): 
            with open("pranisha-food.txt")as pranisha:
                for i in pranisha:
                    print(i,end="")
        elif(f_e==2): 
            with open("pranisha-exercise.txt")as pranisha:
                for i in pranisha:
                    print(i,end="")
        else:
            print("invalid number")        
    
    
    elif(person_retrieve==3):
        f_e=int(input("PRESS 1 to get food-log\n  Press 2 to get exercise-log "))
        if(f_e==1): 
            with open("kristal-food.txt")as kristal:
                for i in kristal:
                    print(i,end="")
        elif(f_e==2): 
            with open("kristal-exercise.txt")as kristal:
                for i in kristal:
                    print(i,end="")
        else:
            print("invalid number")      




print("\t-> WELCOME TO THE HEALTH MANAGEMENT SYSTEM------\n")
print("ENTER 1 FOR LOG THE VALUE")
print("ENTER 2 FOR RETRIEVE THE VALUES")
a=int(input())
if a==1:
    print("PRESS 1 FOR ADITI")    
    print("PRESS 2 FOR PRANISHA")
    print("PRESS 3 FOR KRISTAL")
    person_log=int(input())
    log(person_log)
elif a==2:
    print("PRESS 1 FOR ADITI")    
    print("PRESS 2 FOR PRANISHA")
    print("PRESS 3 FOR KRISTAL")
    person_retrieve=int(input())
    log(person_retrieve)
else:
    print("Invalid choice")


