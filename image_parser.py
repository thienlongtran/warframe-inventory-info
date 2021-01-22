import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def getItemListFromImage(img, item_list):
    img = cropImage(img)
    img = maskImage(img)
    isolateItems(img)
    collection = pytesseract.image_to_string(img)
    collection = beautifyTesseractResults(collection, item_list)
    return collection

def beautifyTesseractResults(collection, item_list):
    collection = collection.split("\n\n") #Seperate items by empty newline
    for i in range(len(collection)):
        collection[i] = collection[i].replace("\n", " ")
        item_list.add(collection[i])
    return collection

def maskImage(img):
    """
    Warframe Text Mask Values;
    Lower HSV: (21, 100, 125)
    Higher HSV: (23, 132, 208)
    """
    lower_gold = (21,100,125)
    higher_gold = (23,132,208)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img = cv2.inRange(img, lower_gold, higher_gold)
    return img

def cropImage(img):
    img = img[200:950, 80:1380]
    return img

def isolateItems(img):
    """
    Split the contents of a cropped Warframe inventory section into individual items.
    Seperate items assuming that inventory is in a 7x4 template.
    Returns a collection of individual images of each item.
    """
    images = []
    height, width = img.shape

    for i in range(7):
        for j in range(4):
            x1 = (int)((i/7) * width)
            x2 = (int)(((i+1)/7) * width)
            y1 = (int)((j/4) * height)
            y2 = (int)(((j+1)/4) * height)
            images.append(img[y1:y2, x1:x2])
    
    return images
