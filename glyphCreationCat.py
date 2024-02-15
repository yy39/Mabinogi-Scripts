import pyautogui
import pydirectinput
import time
import keyboard
import math

runNum = 1
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

pyautogui.confirm(
    text='Because this script moves your mouse and sends clicks, do not touch your computer while it runs. Go touch grass or something,', 
    title='!!! Caution !!!', 
    buttons=['OK', 'Cancel']
)

# Select Mabinogi window
pydirectinput.moveTo(math.floor(mainScreenSizeX / 2), math.floor(mainScreenSizeY / 2))
click()
    
while (True):
    print('************************************')
    print('**  Run #' + str(runNum) + ' | Hold Esc to cancel.  **')
    print('************************************')
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break
    clickAt(683, 78) # Open Glyph Design window
    time.sleep(.2) # Wait for window to open
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Selecing color')
    clickAt(884,737) # Pick color
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Selecting filled circle')
    clickAt(963, 463) # Select filled circle
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Drawing eye...')
    clickAndDragTo(1129, 611, 1145, 611) # Make left eye
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Selecting line')
    clickAt(910, 457) # Select Line
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Drawing mouth...')
    clickAndDragTo(1194, 668, 1179, 680) # Draw mouth part 1
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1180, 679, 1181, 691) # Draw mouth part 2
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1180, 690, 1199, 698) # Draw mouth part 3
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1198, 698, 1229, 684) # Draw mouth part 4
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Drawing head...')
    clickAndDragTo(1229, 539, 1163, 549) # Draw head part 1
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1166, 550, 1110, 491) # Draw head part 2
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1112, 491, 1090, 570) # Draw head part 3
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1090, 570, 1074, 641) # Draw head part 4
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1074, 640, 1076, 671) # Draw head part 5
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1076, 670, 1112, 715) # Draw head part 6
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1111, 714, 1193, 740) # Draw head part 7
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1193, 740, 1229, 743) # Draw head part 8
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Drawing whiskers...')
    clickAndDragTo(1111, 678, 1045, 686) # Draw whisker 1
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1118, 701, 1065, 730) # Draw whisker 2
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAt(936, 463) # Select hollow circle
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAndDragTo(1099, 653, 1117, 653) # Draw blush
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Mirroring image')
    clickAt(1151, 874) # Mirror horizontally
    time.sleep(.2) # Wait for notice to open
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAt(1341, 785) # Confirm
    time.sleep(.2) # Wait for notice to close
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    print('Finalizing...')
    clickAt(1671, 921) # Complete
    time.sleep(.2) # Wait for window to open
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAt(1372, 796) # Agree
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break    
    clickAt(1372, 833) # Complete
    if keyboard.is_pressed('esc'):
        print('Script exited')
        break
    print('Completing glyph...')
    time.sleep(5)
    runNum += 1