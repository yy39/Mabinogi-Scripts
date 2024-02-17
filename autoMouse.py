import pyautogui
import pydirectinput
import config
import time
import math
import keyboard

def click():
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def clickAndDragTo(x1: int, y1: int, x2: int, y2: int):
    pydirectinput.moveTo(x1, y1)
    pydirectinput.mouseDown()
    pydirectinput.moveTo(x2, y2)
    pydirectinput.mouseUp()

def clickAt(x: int, y: int):
    pydirectinput.moveTo(x, y)
    pydirectinput.mouseDown()
    pydirectinput.mouseUp()

def clickMainCenter():
    clickAt(math.floor(config.mainScreenSizeX / 2), math.floor(config.mainScreenSizeY / 2))

def clickImage(image: str, retryCount: int=0): 
    try: 
        imageCoords = pyautogui.locateCenterOnScreen(image, confidence=config.imageConfidence)
    except Exception as e:
        print(f'{type(e).__name__}: Unable to find {image}')
        if retryCount == config.retryMax:
            print('Max retries hit')
            retryCount = 0
            exit()
        retryCount = retryCount + 1
        print(f'Sleeping for {config.sleepDuration} seconds... Then retrying. Attempt {retryCount} of {config.retryMax}')
        time.sleep(config.sleepDuration)
        clickImage(image, retryCount)
    else:
        print(f'image found: {image}')
        retryCount = 0
        clickAt(imageCoords[0], imageCoords[1])

def altClickImage(image: str):
    pydirectinput.keyDown('alt')
    clickImage(image)
    pydirectinput.keyUp('alt')

def checkEsc(): 
    if keyboard.is_pressed('esc'):
        print('Exiting...')
        return True