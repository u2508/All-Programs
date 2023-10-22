# importing required modules
from voicerecog_module import *
from PyPDF2 import PdfReader
import tkinter as tk
from pynput.keyboard import Key, Listener
from tkinter import filedialog
'''def pause(key):
    if key == Key.delete or key == Key.esc:
        exit(print(f'you are on page {i} of {file[len(file)-1]}'))
    
def breakcheck():
    with Listener(on_press = pause) as l2: 
        l2.join()
'''
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# creating a pdf reader object
reader = PdfReader(file_path)

# printing number of pages in pdf file
file=file_path.split("/")
n=int(input('starting page number :- '))
f = open("oops.txt", "w",encoding="utf-8")
# getting a specific page from the pdf file
for i in range(n-1,len(reader.pages)):
    page = reader.pages[i]
    # extracting text from page
    text =format(page.extract_text())
    if text=="":
        import ocr
        text=ocr.extractimg(file_path)
    Speech(text,voice_type='0',speed=200)
    #breakcheck()
    f.writelines(text)
    '''if input('input "stop" to stop')=='stop':
        '''
f.close()