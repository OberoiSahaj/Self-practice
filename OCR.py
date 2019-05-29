from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files (x86)\\Tesseract-OCR\tesseract.exe"
img = Image.open('wr10.jpg')
txt = pytesseract.image_to_string(img, lang= 'eng')
print(txt)