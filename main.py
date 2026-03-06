# Image to String Extract
from PIL import Image # PIL (Pillow) is used for opening and manipulating images
import pytesseract   # pytesseract is used for text extraction from image

image_input = "image.png"
image_open = Image.open(image_input)  
text = pytesseract.image_to_string(image_open)    # Extracting text from the image using pytesseract using image_to_string() function

# write extracted text in a file
with open("extracted_text.txt", "w") as f:
    f.write(text)
print("Extracted text saved to 'extracted_text.txt'.")