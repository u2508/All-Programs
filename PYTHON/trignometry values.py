import math
from math import *
from tkinter import *
from math import tan
from math import sin
from math import cos
from math import *
import os
def SCREEN():
    global main_screen
    global n,m,g
    main_screen= Tk ()
    main_screen.geometry("300x250")
    main_screen.title("trigo value calculator")
    main_screen['bg']='green'
    n=IntVar()
    Label(main_screen,text="enter the value in degree", bg="blue", width="300", height="2", font=("Calibri", 48)).pack()
    Label(main_screen,text="", bg="Green", width="300", height="2", font=("Calibri", 24)).pack()
    angle_entry = Entry(main_screen,font=('calibri',48), textvariable=n).pack()
    Label(main_screen,text="", bg="Green", width="300", height="2", font=("Calibri", 24)).pack()
    Button(main_screen,text="calculate", height="2",bg="aqua",width="30",font=("calibri",24), command = calculation).pack()
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    main_screen.mainloop()
def calculation():
    
    m=n.get()
    g=m*0.018
    a=cos(g)
    b=sin(g) 
    c=tan(g)
    d=1/a 
    e=1/b
    f=1/c
    global calculator
    calculator = Toplevel (main_screen)
    calculator.geometry("300x250")
    calculator.title("trigo value calculator")
    calculator['bg']='red'
    Label(calculator,text=('sin of' ,m,'degrees is',b), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri", 12)).pack()
    Label(calculator,text=("cos of ",m,'degrees is',a), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri", 12)).pack()
    Label(calculator,text=("tan of ",m,'degrees is',c), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri", 12)).pack()
    Label(calculator,text=("cosec of ",m,'degrees is',e), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri", 12)).pack()
    Label(calculator,text=("sec of ",m,'degrees is',d), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri", 12)).pack()
    Label(calculator,text=("cot of ",m,'degrees is',f), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri", 12)).pack()   
    Button(calculator,text="exit the pages", height="2",bg="aqua",width="30",font=("calibri",24), command =distroy).pack()
def distroy():
    calculator.destroy()
    main_screen.destroy()
SCREEN()