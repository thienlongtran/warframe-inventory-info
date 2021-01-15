import cv2
import pytesseract
import image_parser

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("./test_image/pic4.png")
print(image_parser.getItemListFromImage(img))