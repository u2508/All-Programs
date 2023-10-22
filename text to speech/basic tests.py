from voicerecog_module import *
import fitz
import tkinter as tk
import re
from tkinter import filedialog
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
doc = fitz.open(file_path)
article_text = ""
for page in doc:
    article_text+=page.get_text()

# Our next step is to normalize these sentences. Normalization is a process that converts a list of words to a more uniform sequence. This is useful in preparing the text for later processing. By transforming the words to a standard format, other operations are able to work with the data and will not have to deal with issues that might compromise the process.

#This step involves word tokenization, Removing ASCII values, Removing tags of any kind, Part-of-speech tagging, and Lemmatization.

#article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
#article_text = re.sub(r'\s+', ' ', article_text)
# Removing special characters and digits
#formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', article_text)
#print(formatted_article_text)
with  open("runtime_speech.txt", "w") as f:
    f.writelines(formatted_article_text)

Speech(formatted_article_text)