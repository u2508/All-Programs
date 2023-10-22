#import modules
import sys
from tkinter import messagebox
from tkinter import *
import random
from tkinter import simpledialog
from mysql.connector import connection
import mysql.connector
from pyprojectmodule import mariostylegame
from pyprojectmodule import asteriod_smasher
from pyprojectmodule import stylegame
# Designing window for login 
flag2=-1
def login1():
    u = username.get()
    p = password.get()
    n=name_info.get()
    data=(u,p,n)
    mycur.execute("insert into userbase  values(%s,%s,%s);",data)
    connectiondb.commit()
    login()
def root_user():
    global names_info
    global root_screen
    root_screen = Tk()
    root_screen.title("Super User access")
    root_screen.geometry("1335x768")
    root_screen['bg']='red'
    names_info=StringVar()
    Label(root_screen,font=("calibri",48),bg="green", text="Super User access requested").pack()
    Label(root_screen, text="",bg="red", font=("calibri", 48)).pack()
    
    Button(root_screen,font=("calibri",24),bg="blue", text="Activate", command=rootAccess).pack()
    Label(root_screen, text="",bg="red", font=("calibri", 48)).pack()
    
    Label(root_screen,font=("calibri",48),bg="green", text="enter your name or \nsuperadmin passcode to continue").pack()
    Entry(root_screen,font=('calibri',48), textvariable=names_info).pack()
    root_screen.mainloop()
def rootAccess():
    # importing datetime module for now() 
    import datetime 
    global flag2,name
    names=names_info.get()
    if names=="1900" or names=='Vashu@12':
        flag2=1
        name="Welcome back Sir"
        login_sucess()
    if names=="17071208":
        colours=['red','green','blue','yellow','aqua','#F5F5DC','#D2691E','#DC143C','#B8860B','#8B008B','#9932CC','#FFD700','#FF69B4','#32CD32','#9370DB','#F5FFFA','#FFE4E1','#FFA500','#DDA0DD','#C0C0C0','#DB7093','#DA70D6','cyan','#dc143c','#ff1493','#a2006d']
        global root_login_screen,a,b,c,d
        name="Welcome back Sir"
        root_login_screen = Tk()
        root_login_screen.geometry('1335x768')
        root_login_screen.title("Root Login Record Access")
        root_login_screen['bg']=random.choice(colours)
        Label(root_login_screen,text=name, bg="blue", width="300", height="2", font=("Calibri", 48)).pack()
        d=Button(root_login_screen,text="RootUser log", height="1",bg="#FF00FF", width="15",font=("calibri",48), command=rootlog_display).place(x=120,y=250)
        e=Button(root_login_screen,text="User database", height="1",bg="#FF00FF", width="15",font=("calibri",48), command=database_display).place(x=720,y=250)
        f=Button(root_login_screen,text="Policy and Documentation", height="1",bg="#FF00FF", width="22",font=("calibri",48), command=policy).place(x=310,y=500)
    elif names!='1900' or names!='Vashu@12':
        rootkey=messagebox.askyesno('Are you sure','This is not the superadmin passcode, This will be used as your name.',icon='warning')
        if rootkey==True:
            # using now() to get current time 
            x0 = (datetime.datetime.now())
            if x0.day==1:
                a="st"
            elif x0.day==2:
                a="nd"
            elif x0.day==3:
                a="rd"
            else:
                a="th"
            current_time=(x0.strftime("%d"+a+" %B %Y"))+"_"+str(x0.hour)+':'+str(x0.minute)+":"+str(x0.second)
            data=(passkey,current_time,names)
            try:
                mycur.execute("insert into rootuserbase  values(%s,%s,%s);",data)
                connectiondb.commit()            
            except mysql.connector.errors.DataError :
                messagebox.askretrycancel("retry",'Name is a required field of maximum 15 characters. \nPlease enter it.',icon='error' )
            except mysql.connector.errors.ProgrammingError :
                mycur.execute("create table rootuserbase (userpasskey varchar(20),date datetime , name char(15) not null );")
                mycur.execute("insert into rootuserbase  values(%s,%s,%s);",data)
                connectiondb.commit()
            flag2=0
            name="Welcome Back"+names
            login_sucess()
        else:
            root_screen.destroy()
            root_user()
        
def login_verify():
    global username1,password1
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if username1=='root' or username1=='Admin' or username1=='Master User' or username1=='Super User' or username1=='localhost':
        root_user()
    else:
        mycur.execute(
            "select pass from userbase  where user=%s ;",(username1,)
        )
        results=mycur.fetchall()


        if results:
            for i in range(0,mycur.rowcount):
                if results[i][0]==password1:
                    name1()
                    login_sucess()

                else:
                    password_not_recognised()
        else:
            user_not_found()

#popup for user not found
def user_not_found():
    global user_not_found_screen
    
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("USER NOT FOUND")
    user_not_found_screen.geometry("1335x768")
    user_not_found_screen['bg']='red'
    Label(user_not_found_screen,font=("calibri",48),bg="green", text="User Not Found").pack()
    Button(user_not_found_screen,font=("calibri",24),bg="red", text="OK", command=delete_user_not_found_screen).pack()
#Game initialisation commands configuration
def  asteroid():
    asteriod_smasher.main()        
def zerokata():
    from pyprojectmodule import tictactoegui
def mariostuff():
    #mariostylegame.main() 
    from pyprojectmodule import obstacle_dodge
def styleretro2048():
    stylegame.mainstrt()
def rootlog_display():
    mycur.execute("select * from rootuserbase;")
    results=mycur.fetchall()
    global log_screen
    global log_text
    log_screen=Toplevel(root_screen)
    log_screen.title('Root User log display')
    log_screen.geometry("1335x768")
    log_text="Userpasskey \t date and time \t Name\n"
    for i in range(0,len(results)):
        log_text=log_text.title()+str(results[i][0])+'\t'+str(results[i][1])+'\t'+str(results[i][2])+'\n'
    Label(log_screen,text=log_text, bg="blue", width="42", height="7", font=("Calibri", 48)).pack()
    Button(log_screen,text="Exit", height="1",bg="#DB7093", width="15",font=("calibri",48), command=exit).place(x=720,y=550)
    Button(log_screen,text="download log".title(), height="1",bg="aqua",width="15",font=("calibri",48), command=downloadrootlog ).place(x=120,y=550)
def database_display():
    mycur.execute("select * from userbase;")
    results=mycur.fetchall()
    global res_screen
    global res_text
    res_screen=Toplevel(root_screen)
    res_screen.title('user database display')
    res_screen.geometry("1335x768")
    res_text="Username \t Password \t Name\n"
    for i in range(0,len(results)):
        res_text=res_text.title()+results[i][0]+'\t\t'+str(results[i][1])+'\t\t'+results[i][2]+'\n'
    Label(res_screen,text=res_text, bg="blue", width="42", height="7", font=("Calibri", 48)).pack()
    Button(res_screen,text="Exit", height="1",bg="#DB7093", width="15",font=("calibri",48), command=exit).place(x=720,y=550)
    Button(res_screen,text="download log".title(), height="1",bg="aqua",width="15",font=("calibri",48), command = download).place(x=120,y=550) 
# Designing popup for login invalid password
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(mnscreen)
    password_not_recog_screen.title("WRONG USERNAME OR PASSWORD")
    password_not_recog_screen.geometry("1335x768")
    password_not_recog_screen['bg']='RED'
    Label(password_not_recog_screen,bg="orange",font=("calibri",48), text="PLEASE TRY AGAIN ").pack()
    Button(password_not_recog_screen,bg="green", text="OK",font=("calibri",24), command=delete_password_not_recognised).pack()

# Deleting popups

# Designing Main(first) window

def main_account_screen():
    global mnscreen
    mnscreen = Tk()
    mnscreen.geometry("1335x768")

    mnscreen.title("Account Login")
    mnscreen['bg']='red'

    Label(mnscreen,text="hey buddy Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 48)).pack()
    Label(mnscreen,text="",bg="red").pack()
    
    Button(mnscreen,text="Login", height="2",bg="aqua",width="30",font=("calibri",48), command = login).pack()
    
    Label(mnscreen,text="",bg='red').pack()
    
    Button(mnscreen,text="Register", height="2",bg="light green", width="30",font=("calibri",48), command=register).pack()
    mnscreen.mainloop()

def delete_password_not_recognised():
    password_not_recog_screen.destroy()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
    
# Designing popup for login success
def login_sucess():
    colours=['red','green','blue','yellow','aqua','#F5F5DC','#D2691E','#DC143C','#B8860B','#8B008B','#9932CC','#FFD700','#FF69B4','#32CD32','#9370DB','#F5FFFA','#FFE4E1','#FFA500','#DDA0DD','#C0C0C0','#DB7093','#DA70D6','cyan','#dc143c','#ff1493','#a2006d']
    global screen,name,a,b,c,d
    screen = Tk()
    screen.geometry('1335x768')
    screen.title("Login Success")
    screen['bg']=random.choice(colours)
    
    Label(screen,text=name, bg="blue", width="300", height="2", font=("Calibri", 48)).pack()
    
    
    a=Button(screen,text="Asteriod Smasher", height="1",bg="aqua",width="15",font=("calibri",48), command = asteroid).place(x=120,y=200)

    b=Button(screen,text="Tic Tac Toe", height="1",bg="#eda6c4", width="15",font=("calibri",48), command=zerokata).place(x=720,y=375)

    f=Button(screen,text="2048 Game", height="1",bg="#DAA520", width="15",font=("calibri",48), command=styleretro2048 ).place(x=720,y=200)

    c=Button(screen,text="Obstacle Dodge Game", height="1",bg="lime", width="15",font=("calibri",48), command=mariostuff).place(x=120,y=375)    
    
    if flag2!=1:
        #normal root user
        d=Button(screen,text="policy", height="1",bg="#FF00FF", width="15",font=("calibri",48), command=policy).place(x=120,y=550)
        e=Button(screen,text="User database", height="1",bg="#FF00FF", width="15",font=("calibri",48), command=database_display).place(x=720,y=550)
    elif flag2==1:
        #super root user @Utkarsh Gupta
        d=Button(screen,text="RootUser log", height="1",bg="#FF00FF", width="15",font=("calibri",48), command=rootlog_display).place(x=120,y=550)
        e=Button(screen,text="User database", height="1",bg="#FF00FF", width="15",font=("calibri",48), command=database_display).place(x=720,y=550)
    else: 
        d=Button(screen,text="Policy and Documentation", height="1",bg="#FF00FF", width="22",font=("calibri",48), command=policy).place(x=310,y=550)
    screen.mainloop()
def login():
    global login_screen
    login_screen = Toplevel(mnscreen)
    login_screen['bg']='yellow'
    login_screen.title("Login")
    login_screen.geometry("1335x768")
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
    
    name_info=StringVar()

    global registration_sucess_screen
    registration_sucess_screen = Toplevel(mnscreen)
    registration_sucess_screen.geometry("1335x768")
    registration_sucess_screen["bg"]='blue'
    registration_sucess_screen.title("registration sucess")
    Label(registration_sucess_screen, text="Registration Successful", bg="green", font=("calibri", 48)).pack()
    Label(registration_sucess_screen, text="enter your name:",bg="red", font=("calibri", 48)).pack()
    Label(registration_sucess_screen, text="",bg="blue", font=("calibri", 48)).pack()
    name_verify=Entry(registration_sucess_screen,font=('calibri',48), textvariable=name_info)
    name_verify.pack()
    name_info.get()


    Label(registration_sucess_screen, text="",bg="blue", font=("calibri", 48)).pack()
    
    Button(registration_sucess_screen,font=('calibri',48), text="click to Login", width=10, height=1,bg="yellow", command = login1).pack()

# Designing window for registration
def register():
    global register_screen
    register_screen = Toplevel(mnscreen)
    register_screen.title("Register")
    register_screen.geometry("1335x768")
    register_screen['bg']='YELLOW'

    global username
    global password
    
    
    global username_entry
    global password_entry
    global no1,no2,oprt

    

    username = StringVar()
    password = StringVar()
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


def mid():
    global flag,passkey,pswd
    if pswd:
        a=pswd.get()
        if a=='root' or a=='root user' or a=='Root User' or a=='Admin' or a=='Master User' or a=='Super User' or a=='localhost':
            flag=1
            b= simpledialog.askstring(title="sql password",prompt="enter the sql password for viewing database info and other admin functions.")
            if b=='0' or b=='cancel' or b=='CANCEL' or b=='Cancel' or b==None:
                b=messagebox.askokcancel('invalid passkey',"retry entering sql password or cancel to exit.")
                if b=='ok' or b=='Ok' or b=='OK':
                    b=mid()
                else:
                    sys.exit()
            else:
                pass
        else:
            flag=0
            b=a
    passkey=b
    main_screen.destroy()
def init():
    global main_screen,mycur,connectiondb
    main_screen= Tk ()
    main_screen.title("Retro Gamer Hub")
    main_screen.geometry("1335x768")
    main_screen['bg']='green'
    global flag,passkey,pswd
    pswd=StringVar()
    Label(main_screen,text="enter your sql password or Admin passphase", bg="Green", width="300", height="2", font=("Calibri", 36)).pack()
    Label(main_screen,text="", bg="Green", width="300", height="1", font=("Calibri", 24)).pack()
    password_entry = Entry(main_screen,text="sql password",font=('calibri',48), textvariable=pswd).pack()
    Label(main_screen,text="", bg="Green", width="300", height="2", font=("Calibri", 24)).pack()
    Button(main_screen,text="continue", height="2",bg="aqua",width="30",font=("calibri",24), command = mid).pack()
    main_screen.mainloop()

    if flag==1:
        connectiondb = connection.MySQLConnection(host="localhost",user="root",password=passkey,charset="utf8")
        mycur = connectiondb.cursor()
        try:
            mycur.execute("create database login;")
            mycur.execute("use login;")
            mycur.execute("create table userbase (user varchar(10),pass varchar(10));")
            mycur.execute("alter table userbase add(name char(10) default 'user1');")

        except mysql.connector.errors.DatabaseError :
            mycur.execute("use login;")
    
    else:
        
        connectiondb = connection.MySQLConnection(host="localhost",user="root",password=passkey,charset="utf8")
        mycur = connectiondb.cursor()
        try:
            mycur.execute("create database login;")
            mycur.execute("use login;")
            mycur.execute("create table userbase (user varchar(10),pass varchar(10));")
            mycur.execute("alter table userbase add(name char(10) default 'user1');")
    
        except mysql.connector.errors.DatabaseError :
            mycur.execute("use login;")
    flagcheck(flag)
def flagcheck(f):
    if f==1:
        root_user()
    else:
        main_account_screen()
def downloadrootlog():
    global log_text
    text=log_text
    file1=open("rootlog.doc","w+")
    file1.writelines(text)
def download():
    global res_text
    text=res_text
    file1=open("log.doc","w+")
    file1.writelines(text)
def policy():
    policyscreen = Toplevel()
    global policytext
    policyscreen.title("Privacy Policy")
    policyscreen['bg']='red'
    policyscreen.geometry('1335x768')
    policytext="privacy policy".title()+"\n We do not collect any private information from \nuser apart from their sql password and their name. \nWe respect your right to privacy. We try our very\n best to protect your personal information. Never\n give ur personal details to anyone else."+"\nCopyright\xa92023 Utkarsh Gupta"
    
    Label(policyscreen,text=policytext, bg="blue", width="42", height="7", font=("Calibri", 48)).pack()
    Button(policyscreen,text="Exit", height="1",bg="#DB7093", width="15",font=("calibri",48), command=exit).place(x=720,y=550)
    Button(policyscreen,text="download policy".title(), height="1",bg="aqua",width="15",font=("calibri",48), command = downloadpolicy).place(x=120,y=550)
def downloadpolicy():
    global policytext
    text=policytext
    file1=open("policy.doc","w+")
    file1.writelines(text)
def name1():
    global name
    
    mycur.execute(
                "select name from userbase  where user=%s and pass=%s;",(username1,password1)
                )
    n=mycur.fetchall()
    if n!=[]:
        name='Welcome Back ' + str(n[0][0]).capitalize()
    else:
        name='Welcome Back'

if __name__ == '__main__':
    init()
    