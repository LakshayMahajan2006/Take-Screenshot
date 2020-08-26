# Take-Screenshot
#import modules
import pyautogui# pip install pyautogui
from PIL import Image, ImageGrab# pip install pillow
import time

#define a function to take screenshot
def takeScreenshot():
    image = ImageGrab.grab()
    image.show()

if __name__ == "__main__":
    time.sleep(2)# 2 is a time to take screenshot
    takeScreenshot()
