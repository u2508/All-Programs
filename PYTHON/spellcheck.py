from textblob import Word
import re
import tkinter as tk
from tkinter import filedialog
import os
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


def check_word_spelling(word):
    
    word = Word(word)
    
    result = word.spellcheck()
    
    if word == result[0][0]:
        print(f'Spelling of "{word}" is correct!')
        correctword=word
    else:
        print(f'Spelling of "{word}" is not correct!')
        print(f'Correct spelling of "{word}": "{result[0][0]}" (with {result[0][1]} confidence).')
        correctword=result[0][0]
    return correctword

def check_sentence_spelling(sentence):
    
    words = sentence.split()
    
    words = [word.lower() for word in words]
    
    words = [re.sub(r'[^A-Za-z0-9]+', '', word) for word in words]
    correct=""

    for word in words:
        word=check_word_spelling(word)
        correct+=word
    else:
        f = open("temp.txt", "w+")
        f.write(correct)
        f.close()

f = open(file_path, "r",encoding="utf-8")
file=f.readlines()
for i in f.readlines():
    check_sentence_spelling(i)
    print(i)
'''else:
    f.close()
    if os.path.exists(file_path):
        os.remove(file_path)
        os.rename("temp.txt",file_path)
    else:
        print("The file does not exist")'''