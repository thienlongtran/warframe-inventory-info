import cv2
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def getItemListFromImage(img, item_list):
    """
    Read the text from an image and store it into the list of items.

    Args:
        img (ndarray): The image of the Warframe inventory.
        item_list (list): An empty list to store the item names in.
    
    Returns:
        no value (function saves results directly to item_list)
    """
    print(type(img))
    img = cropImage(img)
    img = maskImage(img)
    item_images = isolateItems(img)
    readImages(item_images,item_list)
    beautifyTesseractResults(item_list)

def maskImage(img):
    """
    Isolate the text from the rest of the image by thresholding the specific color of the text.

    Args:
        img (ndarray): The image of the Warframe inventory.

    Returns:
        ndarray: The image with only text remaining in HSV format.
    """
    lower_gold = (21,100,125)
    higher_gold = (23,132,208)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img = cv2.inRange(img, lower_gold, higher_gold)
    return img

def cropImage(img):
    """
    Crop the screen for only the relevant inventory section.

    Args:
        img (ndarray): The image of the Warframe inventory.

    Returns:
        ndarray: The image of only the inventory section containing items.
    """
    #TODO: Allow user to manually define inventory section instead of hard cropping.
    img = img[200:950, 80:1380]
    return img

def isolateItems(img):
    """
    Split the contents of a cropped Warframe inventory section into individual images of individual items.

    Args:
        img (ndarray): The image of the Warframe inventory.

    Returns:
        list: A collection of individual images of each item.
    """

    #IMPORTANT: Function assumes inventory is in a 7x4 template.
    #TODO: Make the function automatically detect row and column numbers.

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

def readImages(item_images, item_list):
    """
    Read the item names from a collection of cleaned images that only contain text.

    Args:
        item_images (list): A list of images of each individual Warframe item in inventory.
        item_list (list): An empty list where the results of the text detection will be directly saved.

    Returns:
        no value (function saves results directly to item_list)
    """
    for i in range(len(item_images)):
        text_result = pytesseract.image_to_string(item_images[i])
        item_list.append(text_result)


def beautifyTesseractResults(item_list):
    """
    Clean up the results of the PyTesseract text detection so that it is more human-readable and useful with Market API

    Args:
        item_list (list): A list of strings of the names of the Warframe items in the inventory.

    Returns:
        no value (function saves results directly to item_list)
    """
    for i in range(len(item_list)):
        item_list[i] = item_list[i].replace("\n", " ")
        item_list[i] = re.sub("\x0c","",item_list[i]) #Remove Page Breaks
        item_list[i] = item_list[i].strip() #Remove Trailing Spaces