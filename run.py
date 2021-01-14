import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread("./test_image/pic4.png")
img = img[0:1080, 80:1400]

cv2.imshow("cropped", img)

"""
Warframe Text Mask Values;
Lower HSV: (21, 100, 125)
Higher HSV: (23, 132, 208)
"""

lower_gold = (21,100,125)
higher_gold = (23,132,208)

img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#cv2.imshow("Result1", img)

img = cv2.inRange(img, lower_gold, higher_gold)

collection = pytesseract.image_to_string(img)
collection = collection.split("\n\n") #Seperate items by empty newline


for i in range(len(collection)):
  collection[i] = collection[i].replace("\n", " ")

print(collection)
cv2.imwrite("Result.jpg", img)
cv2.imshow("Result", img)

cv2.waitKey(0)
