import pyautogui
import pydirectinput
import time

runNum = 1
running = True
while (running):
    print('Run #' + str(run))
    def click():
        time.sleep(.1)
        pydirectinput.mouseDown()
        time.sleep(.1)
        pydirectinput.mouseUp()
        time.sleep(.25)

    def clickAt(imageLocation):
        x = pyautogui.locateCenterOnScreen(imageLocation)[0]
        y = pyautogui.locateCenterOnScreen(imageLocation)[1]
        pydirectinput.moveTo(x, y)
        click()

    print('opening cooking window...')
    clickAt('cooking.png')
    click()
    print('opening dropdown...')
    clickAt('dropdown.png')
    print('selecting boil...')
    pydirectinput.move(-50, 70)
    click()
    print('selecting king crab...')
    pydirectinput.move(0, 80)
    click()
    print('auto registering ingredients...')
    pydirectinput.move(330, 0)
    click()
    print('adding celery...')
    pydirectinput.move(0, 210)
    click()
    pydirectinput.move(-100, 50)
    click()
    print('cooking...')
    time.sleep(5)
    print('done!')
    runNum += 1