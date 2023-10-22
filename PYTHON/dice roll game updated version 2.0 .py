import random
from tkinter import *
import os
import time
def SCREEN():
    global main
    main = Tk ()
    main.geometry("300x250")
    main.title("choice")
    main['bg']='red'
     
    Label(main,text="hey buddy Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 48)).pack()
    Label(main,text="", bg="red", width="300", height="2", font=("Calibri", 48)).pack()
    
    Button(main,text="roll the dice", height="2",bg="aqua",width="30",font=("calibri",48), command = roll).pack()
    main.mainloop()

def roll():
    global roll_screen
    min = 1
    max = 6  
    a=random.randint(min,max)
    roll_screen = Toplevel(main)
    roll_screen['bg']='yellow'
    roll_screen.title("Login")
    roll_screen.geometry("300x250")
    Label(roll_screen,text="The values are....",bg="red",font=("Calibri", 48)).pack()
    Label(roll_screen,text= a, bg="yellow", width="300", height="2", font=("Calibri", 48,"bold")).pack()
    Button(roll_screen,text="roll the dice", height="2",bg="aqua",width="30",font=("calibri",48), command = roll).pack()
    Button(roll_screen,text="exit the pages", height="2",bg="aqua",width="30",font=("calibri",48), command = distroy).pack()
def distroy():
    roll_screen.destroy()
    main.destroy()
SCREEN()