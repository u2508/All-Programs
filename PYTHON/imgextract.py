from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import cv2
import pytesseract 

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

root = Tk()
root.title('Text Extraction from image project') 

newline= Label(root)
uploaded_img=Label(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )


def extract(path):
    Actual_image = cv2.imread(path)
    Sample_img = cv2.resize(Actual_image,(400,350))
    Image_ht,Image_wd,Image_thickness = Sample_img.shape
    Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BGR2RGB)
    texts = pytesseract.image_to_string(Sample_img) 
    Label(root,text=texts,font=('Times',15,'bold'),bg="blue",fg="red").place(x=450,y=400)
    print(texts)

def show_extract_button(path):
    extractBtn= Button(root,text="Extract text",command=lambda: extract(path),bg="#2f2f77",fg="gray",pady=15,padx=15,font=('Times',15,'bold'))
    extractBtn.place(x=1080,y=10)

def upload():
    try:
        path=filedialog.askopenfilename()
        image=cv2.imread(path)
        Sample_img = cv2.resize(image,(400,350))
        Sample_img = cv2.cvtColor(Sample_img,cv2.COLOR_BAYER_GB2RGB)
        uploaded_img.configure(image=Sample_img)
        uploaded_img.image=Sample_img
        show_extract_button(path)
    except:
        pass  

uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="red",height=2,width=20,font=('Times',15,'bold')).place(x=340,y=10)
newline.configure(text='\n')
newline.pack()
uploaded_img.place(x=500,y=100)

root.mainloop()