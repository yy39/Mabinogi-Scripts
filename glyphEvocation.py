import pyautogui
import pydirectinput
import time
import autoMouse
import config

runNum = 1
glyphNum = 1

choice = pyautogui.confirm(
    text='Because this script moves your mouse and sends clicks, do not touch your computer while it runs.\r\rMake sure your inventory is open and that all your glyph imprints have max uses prior to pressing ok and then go touch grass or something.', 
    title='!!! Caution !!!', 
    buttons=['OK', 'Cancel']
)

# Select Mabinogi window
autoMouse.clickMainCenter()
    
if (choice == 'OK'):
    while (True):
        if (runNum > config.glyphUseCount): 
            print('[ Imprint exhausted, disposing and resetting use count... ]')
            if autoMouse.checkEsc():
                break
            autoMouse.clickImage('trash')
            time.sleep(.2)
            if autoMouse.checkEsc():
                break
            autoMouse.altClickImage('redGlyph')
            autoMouse.clickAt(1408, 947)
            time.sleep(.2)
            if autoMouse.checkEsc():
                break
            autoMouse.clickAt(1357,787)
            if autoMouse.checkEsc():
                break
            runNum = 1
            glyphNum += 1
        else:
            print(f'[ Glyph Imprint #{glyphNum} | Imprint Uses: {runNum}/{config.glyphUseCount} | Hold Esc to cancel. ]')
            autoMouse.clickAt(736, 76)
            time.sleep(.2)
            if autoMouse.checkEsc():
                break
            autoMouse.clickAt(911, 537)
            if autoMouse.checkEsc():
                break
            autoMouse.clickAt(1222, 884)
            time.sleep(.2)
            if autoMouse.checkEsc():
                break
            autoMouse.clickAt(1338, 792)
            time.sleep(.2)
            if autoMouse.checkEsc():
                break
            autoMouse.clickAt(1338, 838)
            time.sleep(10)
            if autoMouse.checkEsc():
                break
            runNum += 1
else:
    print('Script cancelled')