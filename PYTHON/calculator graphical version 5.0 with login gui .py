#import modules
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import os
# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
    register_screen['bg']='YELLOW'

    global username
    global password
    global name
    global username_entry
    global password_entry
    global name_entry
    username = StringVar()
    password = StringVar()
    name =StringVar()
    Label(register_screen,font=('calibri',48) ,text="Please enter details below", bg="blue").pack()
    
    Label(register_screen,font=('calibri',24), bg="yellow",text="").pack()
    username_lable = Label(register_screen,bg="red",font=('calibri',48), text="Username * ").pack()
    Label(register_screen,font=('calibri',24),bg="yellow", text="").pack()
    username_entry = Entry(register_screen,bg="orange",font=('calibri',48), textvariable=username).pack()
    Label(register_screen,font=('calibri',24), text="",bg="yellow").pack()
    password_lable = Label(register_screen,bg="green",font=('calibri',48), text="Password * ").pack()
    Label(register_screen,font=('calibri',24),bg="yellow", text="").pack()
    password_entry = Entry(register_screen,bg="brown",font=('calibri',48), textvariable=password, show='*').pack()
    Label(register_screen,font=('calibri',24),bg="yellow", text="").pack()
    Button(register_screen, text="Register", width=10,font=('calibri',48), height=1, bg="pink", command =registration_sucess).pack()


# Designing window for login 

def login():
    global login_screen
    login_screen = Toplevel(screen)
    login_screen['bg']='yellow'
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen,font=("calibri",48,"bold"),bg="pink", text="Please enter details below to login").pack()
    Label(login_screen,bg="yellow", text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen,bg="red",font=('calibri',48), text="Username * ").pack()
    Label(login_screen,font=('calibri',24),bg="yellow", text="").pack()
    username_login_entry = Entry(login_screen,font=('calibri',48), textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen,font=('calibri',24),bg="yellow", text="").pack()
    Label(login_screen,bg="blue",font=('calibri',48), text="Password * ").pack()
    Label(login_screen,font=('calibri',24), bg="yellow",text="").pack()
    password_login_entry = Entry(login_screen,font=('calibri',48), textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen,font=('calibri',24),bg="yellow", text="").pack()
    Button(login_screen,font=('calibri',24), text="Login", width=10, height=1,bg="yellow", command = login_verify).pack()

# Implementing event on register button
def registration_sucess():
    global name_info
    username_info = username.get()
    password_info = password.get()
    file = open(username_info,"w")
    file.write(username_info + "\n")
    file.write(password_info +"\n")
    file.close()

    global registration_sucess_screen
    registration_sucess_screen = Toplevel(screen)
    
    registration_sucess_screen["bg"]='blue'
    registration_sucess_screen.title("registration sucess")
    Label(registration_sucess_screen, text="Registration Success", bg="green", font=("calibri", 48)).pack()
    Label(registration_sucess_screen, text="",bg="blue", font=("calibri", 48)).pack()
    Button(registration_sucess_screen,font=('calibri',48), text="click to Login", width=10, height=1,bg="yellow", command = login).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(screen)
    password_not_recog_screen.title("wrong password")
    password_not_recog_screen.geometry("150x100")
    password_not_recog_screen['bg']='RED'
    Label(password_not_recog_screen,bg="orange",font=("calibri",48), text="Invalid Password ").pack()
    Button(password_not_recog_screen,bg="green", text="OK",font=("calibri",24), command=delete_password_not_recognised).pack()

# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("USER NOT FOUND")
    user_not_found_screen.geometry("150x100")
    user_not_found_screen['bg']='red'
    Label(user_not_found_screen,font=("calibri",48),bg="green", text="User Not Found").pack()
    Button(user_not_found_screen,font=("calibri",24),bg="red", text="OK", command=delete_user_not_found_screen).pack()

# Deleting popups

def delete_login_success():
    screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()
def  graphical():
    global main_screen
    global no,o,op
    main_screen= Tk ()
    main_screen.geometry("300x250")
    main_screen.title("Graphical Calculator")
    main_screen['bg']='green'
    no = IntVar()
    o = IntVar()
    op=StringVar()
    Label(main_screen,text="enter first no.", bg="blue", width="300", height="2", font=("Calibri", 24)).pack()
    e1 = Entry(main_screen,font=('calibri',24),bg="maroon" , textvariable=no).pack()
    Label(main_screen,text="enter second no.", bg="blue", width="300", height="2", font=("Calibri",24)).pack()
    e2 = Entry(main_screen,font=('calibri',24),bg="maroon" ,textvariable=o).pack()
    Label(main_screen,text="enter operator", bg="blue", width="300", height="2", font=("Calibri",24)).pack()
    e3 = Entry(main_screen,font=('calibri',24),bg="maroon", textvariable=op).pack()
    Button(main_screen,text="calculate", height="2",bg="aqua",width="30",font=("calibri",24), command = calculation(no,o,op) ).pack()
    Button(main_screen,text="exit the pages", height="2",bg="aqua",width="30",font=("calibri",24), command =ExitApplication ).pack()
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
    Label(main_screen,text="", bg="red", width="300", height="2", font=("Calibri", 24)).pack()
def calculation(a,b,opt):
    res=IntVar()
    
    if opt=="*" :
        res=a*b
    elif opt == "/":
        res=a/b
    elif opt == "+":
        res= a + b
    elif opt == "-":
        res=a-b
    elif opt == 'square of a':
        res=a*a   
    elif opt == 'square of b':
        res=b*b
    elif opt == 'cube of a':
        res=a*a*a
    elif opt == 'cube of b':
        res=b*b*b
    elif opt == 'a sq - b sq':
        res=(a*a)-(b*b)
    elif opt == '(a+b)sq':
        res=(a+b)*(a+b)
    elif opt == '(a+b)sq':
        res=(a-b)*(a-b)
    elif opt == 'a sq + b sq':
        res=(a*a)+(b*b)
    elif opt == 'a cube - b cube':
        res=(a*a*a)-(b*b*b)
    elif opt == 'a cube + b cube':
        res=(a*a*a)+(b*b*b)
    elif opt == '(a+b) cube':
        res=(a+b)*(a+b)*(a+b)
    elif opt == '(a-b) cube':
        res=(a-b)*(a-b)*(a-b)
    elif opt == 'sq rt of a':
        res=math.sqrt(a)
    elif opt == 'sq rt of b':
        res=math.sqrt(b)
    elif opt == 'cube rt of a':
        res=a**(1/3)
    elif opt == 'cube rt of b':
        res=b**(1/3)
    elif opt=='check remainder of a/b' or opt=='mod of a/b' or opt=='mod a/b' :
        res= a % b
    elif opt=='check remainder of b/a' or opt=='mod of b/a' or opt=='mod b/a' :
        res=b % a
    else:
        res='-1'    
    global calculator
    calculator = Toplevel (main_screen)
    calculator.geometry("300x250")
    calculator.title("result")
    calculator['bg']='red'
    Label(calculator,text=('result page'), bg="Green", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text="", bg="red", width="300", height="1", font=("Calibri",24)).pack()
    Label(calculator,text=('The result is'), bg="blue", width="300", height="1", font=("Calibri", 36)).pack()
    Label(calculator,text= res, bg="red", width="300", height="1", font=("Calibri", 24)).pack()   
    Button(calculator,text="exit the pages", height="2",bg="aqua",width="30",font=("calibri",24), command =ExitApplication).pack()
def distroy():
    main_screen.destroy()
def ExitApplication():
    MsgBox = tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
    if MsgBox == 'yes':
       distroy()
       delete_login_success()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application screen')

# Designing popup for login success
def login_sucess():
    graphical()

# Designing Main(first) window

def main_account_screen():
    global screen
    screen = Tk()
    screen.geometry("300x250")
    screen.title("Account Login")
    screen['bg']='red'
    Label(text="hey buddy Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 48)).pack()
    Label(text="",bg="red").pack()
    Button(text="Login", height="2",bg="aqua",width="30",font=("calibri",48), command = login).pack()
    Label(text="",bg='red').pack()
    Button(text="Register", height="2",bg="light green", width="30",font=("calibri",48), command=register).pack()
    screen.mainloop() 
main_account_screen()