import fitz
import tkinter as tk
from time import sleep
from pynput.keyboard import Key, Listener
from tkinter import ttk, filedialog, messagebox, simpledialog
from voicerecog_module import Speech
import re
import logging
import logging.handlers
from ttkthemes import ThemedTk
import gettext

# Set up logging to both console and file
log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
log_handler = logging.handlers.RotatingFileHandler('text to speech\\pdf_processor.log', maxBytes=1024*1024, backupCount=5)
log_handler.setFormatter(log_formatter)
root_logger = logging.getLogger()
root_logger.addHandler(log_handler)
root_logger.setLevel(logging.INFO)

# Internationalization
gettext.bindtextdomain("pdf_processor", "locale")
gettext.textdomain("pdf_processor")
_ = gettext.gettext

class PDFProcessor:
    def __init__(self):
        self.root = ThemedTk(theme="arc")  # Use ttkthemes for better styling
        self.root.title(_("PDF Processor"))
        self.root.withdraw()
        self.is_cancelled=False
        self.process_pdf()
    def process_pdf(self):
        try:
            file_path = self.select_pdf_file()
            if not file_path:
                return

            formatted_article_text = self.extract_text(file_path)
            if not formatted_article_text:
                return

            save_path = self.save_text_to_file(formatted_article_text)
            self.run_speech(formatted_article_text)

            messagebox.showinfo(_("Info"), _("Text saved to '{save_path}'.").format(save_path=save_path))
        except FileNotFoundError:
            logging.error(_("File not found."))
            messagebox.showerror(_("Error"), _("File not found."))
            exit(logging.info(_("errors were found . Termination requested.")))
        except Exception as e:
            error_message = _("An error occurred: {e}").format(e=e)
            logging.error(error_message)
            messagebox.showerror(_("Error"), error_message)
            exit(logging.info(_("errors were found. Termination requested.")))

    def select_pdf_file(self):
        file_path = filedialog.askopenfilename(filetypes=[(_("PDF files"), "*.pdf")])
        return file_path

    def extract_text(self, file_path):
        formatted_article_text = ""

        try:
            doc = fitz.open(file_path)
            num_pages = doc.page_count
            
            n=self.choose_page(num_pages)
            progress_window = self.create_progress_window(_("Extracting Text"), num_pages)
            self.is_cancelled = False
            if n==None:
                n=1
            page_texts = []
            for page_num in range(n-1,num_pages):
                if self.is_cancelled:
                    break
                page_text = self.extract_page_text(doc, page_num)
                
                page_texts.append(page_text)
                self.update_progress(progress_window, page_num + 1)
                #sleep(0.25)
            formatted_article_text = " ".join(page_texts)
            progress_window.destroy()
            doc.close()

        except fitz.FileNotFoundError:
            logging.error('FILE NOT FOUND ERROR' )           
            messagebox.showerror(_("Error"), 'FILE NOT FOUND ERROR')
            exit(logging.info(_("errors were found.termination requested.")))
        except Exception as e:
            error_message = _("An error occurred during PDF processing: {e}").format(e=e)
            logging.error(error_message)
            messagebox.showerror(_("Error"), error_message)
            exit(logging.info(_("errors were found. Termination requested.")))

        return formatted_article_text

    def extract_page_text(self, doc, page_num):
        page = doc[page_num]
        return page.get_text()

    def save_text_to_file(self, text):
        try:
            formatted_text = re.sub(r'\s+', ' ', text)
            save_path = "text to speech\\runtime_speech.txt"
            with open(save_path, "w",encoding="utf-8") as f:
                f.write(formatted_text)
            logging.info(_("Formatted text saved to '{save_path}'.").format(save_path=save_path))
            with open("dataset.txt",'a',encoding="utf-8") as f1:
                f1.write(formatted_text)
            return save_path
        except Exception as e:
            error_message = _("An error occurred while saving text to file: {e}").format(e=e)
            logging.error(error_message)
            messagebox.showerror(_("Error"), error_message)
            exit(logging.info(_("errors were found. Termination requested.")))
    def pause(self,key):
        if key == Key.delete or key == Key.esc:
            exit()
        if format(key)[1]=='>'or format(key)[1]=='<':
            if format(key)[1]=='>':
                self.speed+=0.25
            else :
                self.speed-=0.25
            print ("speed is ",self.speed)
        
        if key==Key.right or key==Key.left:
            if key==Key.right:
                self.speed+=0.5
            else:
                self.speed-=0.5
            print ("speed is ",self.speed)
     

    def breakcheck(self,text):
        with Listener(on_press = self.pause) as l2: 
            Speech(text, voice_type=self.voice_type, speed=self.speed)
            l2.join()
    def run_speech(self, text):
        try:
            self.voice_type = self.choose_voice_type()
            self.speed = self.choose_speech_speed()
            self.breakcheck(text)
            logging.info(_("Speech processing completed."))
            logging.info(_("Execution successful. No errors were found."))
        except Exception as e:
            error_message = _("An error occurred during speech processing: {e}").format(e=e)
            logging.error(error_message)
            messagebox.showerror(_("Error"), error_message)
            exit(logging.info(_("errors were found. Termination requested.")))

    def choose_voice_type(self):
        return simpledialog.askstring(_("Voice Type"), _("Enter voice type (e.g., male, female):"))

    def choose_speech_speed(self):
        return simpledialog.askinteger(_("Speech Speed"), _("Enter speech speed (words per minute):"), minvalue=50, maxvalue=400)
    
    def choose_page(self,n):
        return simpledialog.askinteger(_("Starting page"), _("Enter starting page:"), minvalue=0, maxvalue=n)
    def create_progress_window(self, title, total):
        progress_window = tk.Toplevel(self.root)
        progress_window.title(title)

        label = tk.Label(progress_window, text=_("Extracting text..."))
        label.pack(pady=10)  # Add some padding to the top

        progress = ttk.Progressbar(progress_window, length=250, mode="determinate", maximum=total)
        progress.pack(pady=5)  # Add padding around the progress bar

    # Use a frame for the button to ensure it's visible
        button_frame = tk.Frame(progress_window)
        button_frame.pack(pady=5)

        cancel_button = ttk.Button(button_frame, text=_("Cancel"), command=self.cancel_extraction)
        cancel_button.pack()  # Pack the button inside the frame

        return progress_window


    def update_progress(self, progress_window, value):
        progress_widgets = progress_window.winfo_children()
        for widget in progress_widgets:
            if isinstance(widget, ttk.Progressbar):
                widget["value"] = value
                self.root.update_idletasks()
                break

    def cancel_extraction(self):
        self.is_cancelled = True
        exit()

    def start(self):
        self.root.mainloop()

def main():
    pdf_processor = PDFProcessor()
    pdf_processor.start()

if __name__ == "__main__":
    main()
