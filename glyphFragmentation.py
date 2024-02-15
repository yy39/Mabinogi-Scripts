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
    text='! THIS SCRIPT WILL FRAGMENT ANY AND ALL VISIBLE GLYPHS !\r\rBecause this script moves your mouse and sends clicks, do not touch your computer while it runs. Go touch grass or something \r\rBefore proceeding, ensure the below conditions are met: \r\r1. Close/Minimize any open bags containing the glyphs you wish to keep.\r\r2. Make sure the Fragmentation skill is set on a visible hotbar and not grayed out.\r\r3. Ensure Interface Color is [Neon Pink] & [Opaque].\r\r4. Your hands are free.\r\r 5. There are no open windows. (Inventory is okay)\r\r 6. Ensure glyphs do not have "NEW" by mousing over them.\r\r! THIS SCRIPT WILL FRAGMENT ANY AND ALL VISIBLE GLYPHS !', 
    title='!!! Caution !!!', 
    buttons=['OK', 'Cancel']
)
# Select Mabinogi window
clickAt(math.floor(mainScreenSizeX / 2), math.floor(mainScreenSizeY / 2))
    
while (True):
    if choice == 'OK':
        print(f'Glyph Fragmentation #{runNum} | Hold Esc to cancel')
        if keyboard.is_pressed('esc'):
            print('Script exited')
            break
        clickAt(pyautogui.locateCenterOnScreen('fragmentation.png', confidence=0.9)[0], pyautogui.locateCenterOnScreen('fragmentation.png', confidence=0.9)[1])
        time.sleep(.2)
        if keyboard.is_pressed('esc'):
            print('Script exited')
            break
        pydirectinput.keyDown('alt')
        clickAt(pyautogui.locateCenterOnScreen('glyph.png', confidence=0.9)[0], pyautogui.locateCenterOnScreen('glyph.png', confidence=0.9)[1])
        pydirectinput.keyUp('alt')
        time.sleep(.2)
        clickAt(pyautogui.locateCenterOnScreen('fragmentationButton.png', confidence=0.9)[0], pyautogui.locateCenterOnScreen('fragmentationButton.png', confidence=0.9)[1])
        if keyboard.is_pressed('esc'):
            print('Script exited')
            break
        time.sleep(6)
        runNum += 1
    else:
        break