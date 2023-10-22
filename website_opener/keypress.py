from pynput.keyboard import Key, Listener
import os
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
from os import system
def main():
    system("\"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe\" -incognito https://xvideos.wapka.cc/")
    kill()
def keypressencounter(site,incog=0):
    if incog==1:
        system(f"\"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe\" -incognito {site}")
    else:
        system(f"\"C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe\" {site}")
    kill()
def option1():
    
    root.destroy()
    keypressencounter("https://www.google.com/")
def option2():
    
    root.destroy()
    keypressencounter("https://www.youtube.com/")
def option3():
    
    root.destroy()
    keypressencounter("https://chat.openai.com/")
def option4():
    b= simpledialog.askinteger(title="PASSWORD Window",prompt="enter the four digit security code.")
    if b == 1900 :
        entry=simpledialog.askstring(title="site entry",prompt="enter the site to be opened in incognito mode:- ")
        if entry =="0":
            root.destroy()
            main()
            
        else:
            root.destroy()
            keypressencounter(entry,1)
            
        
    else:
        messagebox.askokcancel('access denied','try again later',icon='error')
        exit()
def window():
    global root
    root = tk.Tk()
    root.title("Options Menu")

    tk.Button(root, text="google", command=option1).pack()
    tk.Button(root, text="youtube", command=option2).pack()
    tk.Button(root, text="chatgpt", command=option3).pack()
    tk.Button(root, text="incognito", command=option4).pack()

    root.mainloop()

def show(key):
    print(key)
    if format(key)[1]=='w':
        os.system(("taskkill /IM brave.exe "))
        return False
    # by pressing 'delete' button
    # you can terminate the loop
    elif key == Key.delete:
        exit()
        return False
    elif key == Key.f10 or format(key)[1]=='r':
        exit(os.system('C:/Users/utkar/AppData/Local/Programs/Python/Python39/python.exe c:/Users/utkar/OneDrive/vscode/alon.py'))    
# Collect all event until released
def  kill():
    with Listener(on_press = show) as l1:
	    l1.join()
if __name__ == '__main__':
    site=input("enter site name or type 'default' to show the default site options or incognito site opening:-")
    if site =="default":
        window()
    else:
        keypressencounter(site)