import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("pic.png")

"""
Warframe Text Mask Values;
Lower HSV: (21, 100, 125)
Higher HSV: (23, 132, 208)
"""

lower_gold = (21,100,125)
higher_gold = (23,132,208)

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

img = cv2.inRange(img, lower_gold, higher_gold)
cv2.imshow("Result",img)
cv2.waitKey(0)