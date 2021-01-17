import cv2
import pyautogui
import numpy
from pynput import keyboard
import image_parser

def execute():
    img = cv2.cvtColor(numpy.array(pyautogui.screenshot()),cv2.COLOR_RGB2BGR)
    image_parser.getItemListFromImage(img, item_list)

def on_press(key):
    print('{0} pressed'.format(key))
    if key == keyboard.Key.print_screen:
        execute()

def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener
        print(item_list)
        return False

item_list = {""}
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()