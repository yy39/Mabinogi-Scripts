import pyautogui
import time
import autoMouse 

runNum = 1

pyautogui.confirm(
    text='Because this script moves your mouse and sends clicks, do not touch your computer while it runs. Go touch grass or something,', 
    title='!!! Caution !!!', 
    buttons=['OK', 'Cancel']
)

# Select Mabinogi window
autoMouse.clickMainCenter()
    
while (True):
    print('************************************')
    print('**  Run #' + str(runNum) + ' | Hold Esc to cancel.  **')
    print('************************************')
    if autoMouse.checkEsc():
        break
    autoMouse.clickAt(683, 78) # Open Glyph Design window
    time.sleep(.2) # Wait for window to open
    if autoMouse.checkEsc():
        break    
    print('Selecing color')
    autoMouse.clickAt(884,737) # Pick color
    if autoMouse.checkEsc():
        break    
    print('Selecting filled circle')
    autoMouse.clickAt(963, 463) # Select filled circle
    if autoMouse.checkEsc():
        break    
    print('Drawing eye...')
    autoMouse.clickAndDragTo(1129, 611, 1145, 611) # Make left eye
    if autoMouse.checkEsc():
        break    
    print('Selecting line')
    autoMouse.clickAt(910, 457) # Select Line
    if autoMouse.checkEsc():
        break    
    print('Drawing mouth...')
    autoMouse.clickAndDragTo(1194, 668, 1179, 680) # Draw mouth part 1
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1180, 679, 1181, 691) # Draw mouth part 2
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1180, 690, 1199, 698) # Draw mouth part 3
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1198, 698, 1229, 684) # Draw mouth part 4
    if autoMouse.checkEsc():
        break    
    print('Drawing head...')
    autoMouse.clickAndDragTo(1229, 539, 1163, 549) # Draw head part 1
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1166, 550, 1110, 491) # Draw head part 2
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1112, 491, 1090, 570) # Draw head part 3
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1090, 570, 1074, 641) # Draw head part 4
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1074, 640, 1076, 671) # Draw head part 5
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1076, 670, 1112, 715) # Draw head part 6
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1111, 714, 1193, 740) # Draw head part 7
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1193, 740, 1229, 743) # Draw head part 8
    if autoMouse.checkEsc():
        break    
    print('Drawing whiskers...')
    autoMouse.clickAndDragTo(1111, 678, 1045, 686) # Draw whisker 1
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1118, 701, 1065, 730) # Draw whisker 2
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAt(936, 463) # Select hollow circle
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAndDragTo(1099, 653, 1117, 653) # Draw blush
    if autoMouse.checkEsc():
        break    
    print('Mirroring image')
    autoMouse.clickAt(1151, 874) # Mirror horizontally
    time.sleep(.2) # Wait for notice to open
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAt(1341, 785) # Confirm
    time.sleep(.2) # Wait for notice to close
    if autoMouse.checkEsc():
        break    
    print('Finalizing...')
    autoMouse.clickAt(1671, 921) # Complete
    time.sleep(.2) # Wait for window to open
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAt(1372, 796) # Agree
    if autoMouse.checkEsc():
        break    
    autoMouse.clickAt(1372, 833) # Complete
    if autoMouse.checkEsc():
        break
    print('Completing glyph...')
    time.sleep(5)
    runNum += 1