import pyautogui
import time
import keyboard
import autoMouse
import config

choice = pyautogui.confirm(
    text='! THIS SCRIPT WILL FRAGMENT ANY AND ALL VISIBLE GLYPHS !\r\rBecause this script moves your mouse and sends clicks, do not touch your computer while it runs. Go touch grass or something \r\rBefore proceeding, ensure the below conditions are met: \r\r1. Close/Minimize any open bags containing the glyphs you wish to keep.\r\r2. Make sure the Fragmentation skill is set on a visible hotbar and not grayed out.\r\r3. Ensure Interface Color is [Neon Pink] & [Opaque].\r\r4. Your hands are free.\r\r 5. There are no open windows. (Inventory is okay)\r\r 6. Ensure glyphs do not have "NEW" by mousing over them.\r\r! THIS SCRIPT WILL FRAGMENT ANY AND ALL VISIBLE GLYPHS !', 
    title='!!! Caution !!!', 
    buttons=['OK', 'Cancel']
)

if choice == 'OK':
    runNum = 1

    # Select Mabinogi window
    autoMouse.clickMainCenter()
        
    while (True):
        print(f'Glyph Fragmentation #{runNum} | Hold Esc to cancel')
        if keyboard.is_pressed('esc'):
            print('Script exited')
            break
        autoMouse.clickImage('images/fragmentationSkill')
        time.sleep(.2)
        if keyboard.is_pressed('esc'):
            print('Script exited')
            break
        autoMouse.altClickImage('images/glyph')
        time.sleep(.2)
        autoMouse.clickImage('images/fragmentationButton')
        if keyboard.is_pressed('esc'):
            print('Script exited')
            break
        time.sleep(6)
        runNum += 1
else:
    print('Script cancelled')