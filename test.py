import pyautogui
import pydirectinput
import time
import math

runNum = 1
running = True
mainScreenSizeX = pyautogui.size()[0]
mainScreenSizeY = pyautogui.size()[1]

def click():
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def clickAndDragTo(x1, y1, x2, y2):
    pydirectinput.moveTo(x1, y1)
    pydirectinput.mouseDown()
    pydirectinput.moveTo(x2, y2)
    pydirectinput.mouseUp()

def clickAt(x, y):
    pydirectinput.moveTo(x, y)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

print(pyautogui.locateCenterOnScreen('redGlyph.png'))