#from PIL import Image
#import cv2
import pytesseract


# # set the path of the Tesseract-OCR file

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract'

text = pytesseract.image_to_string('C:/Users/Khin Thandar Kyaw/Pictures/test_v2/amen.png', lang = 'mya')

file = open('language.txt', 'w', encoding = 'utf-8')
file.write(text)
file.close()


