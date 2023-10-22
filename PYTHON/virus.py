import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import sys
import taskcheck as block
def virus():
    code = 1900
    root = tk.Tk()
    root.withdraw()
    a=messagebox.askquestion("corrupt windows","this system has been corrupted. do you want to rescue it?",icon="warning")
    block.getTasks("task")
    if a == 'yes':
        b= simpledialog.askinteger(title="rescue window",prompt="enter the four digit security code to disable the virus")
        block.getTasks("task")
        if b == code :
            sys.exit()
        else:
            messagebox.askokcancel('retry','try again later',icon='error')
            
    else:
        messagebox.askokcancel('relax','This is a fake virus.\nUse the task manager to terminate it.',icon='info')
        
while True:
    virus()
    block.getTasks('task')
    