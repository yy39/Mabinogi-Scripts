import pyautogui
import pydirectinput
import time
import keyboard
import math

runNum = 1
glyphNum = 1
glyphUseCount = 10
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

choice = pyautogui.confirm(
    text='Because this script moves your mouse and sends clicks, do not touch your computer while it runs.\r\rMake sure your inventory is open and that all your glyph imprints have max uses prior to pressing ok and then go touch grass or something.', 
    title='!!! Caution !!!', 
    buttons=['OK', 'Cancel']
)

# Select Mabinogi window
clickAt(math.floor(mainScreenSizeX / 2), math.floor(mainScreenSizeY / 2))
    
while (True):
    if (choice == 'OK'):
        if (runNum > glyphUseCount): 
            print('[ Imprint exhausted, disposing and resetting use count... ]')
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            clickAt(pyautogui.locateCenterOnScreen('trash.png', confidence=0.9)[0], pyautogui.locateCenterOnScreen('trash.png', confidence=0.9)[1])
            time.sleep(.2)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            pydirectinput.keyDown('alt')
            time.sleep(.1)
            clickAt(pyautogui.locateCenterOnScreen('redGlyph.png', confidence=0.9)[0], pyautogui.locateCenterOnScreen('redGlyph.png', confidence=0.9)[1])
            pydirectinput.keyUp('alt')
            clickAt(1408, 947)
            time.sleep(.2)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            clickAt(1357,787)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            runNum = 1
            glyphNum += 1
        else:
            print(f'[ Glyph Imprint #{glyphNum} | Imprint Uses: {runNum}/{glyphUseCount} | Hold Esc to cancel. ]')
            clickAt(736, 76)
            time.sleep(.2)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            clickAt(911, 537)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            clickAt(1222, 884)
            time.sleep(.2)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            clickAt(1338, 792)
            time.sleep(.2)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            clickAt(1338, 838)
            time.sleep(10)
            if keyboard.is_pressed('esc'):
                print('Script exited')
                break
            runNum += 1
    else:
        break