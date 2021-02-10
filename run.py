import cv2
import pyautogui
import numpy
from pynput import keyboard
import image_parser
import excel_handler

def execute():
    img = cv2.cvtColor(numpy.array(pyautogui.screenshot()),cv2.COLOR_RGB2BGR)
    image_parser.getItemListFromImage(img, item_list)

def on_press(key):
    #Activate Screen Capture When Printscreen Key Pressed
    if key == keyboard.Key.print_screen:
        print('{0} pressed. Taking screenshot now...'.format(key))
        execute()

def on_release(key):
    #End Image Capturing Sequence When Escape Key Pressed
    if key == keyboard.Key.esc:
        # Stop listener
        print('{0} released. Saving item to Excel file...'.format(key))
        print(list((filter(None,item_list)))) #Print a cleaned version (without empty strings) of the item list
        excel_handler.itemListToExcel(list((filter(None,item_list)))) #Parse the cleaned version of item list to the Excel handler
        return False

item_list = []
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
