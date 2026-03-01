import pyttsx3 
import pypdf
from tkinter.filedialog import *

book = askopenfilename()
pdfreader = pypdf.PdfReader(book)

pages = len(pdfreader.pages)       # total number of pages in the pdf

for num in range(pages):
    page = pdfreader.pages[num]
    text = page.extract_text()
    speaker = pyttsx3.init()    # text to speech conversion
    speaker.say(text)            
    speaker.runAndWait()
