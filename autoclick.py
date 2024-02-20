import pydirectinput
import time

while (True):
    time.sleep(.1)
    pydirectinput.mouseDown()
    time.sleep(.1)
    pydirectinput.mouseUp()
    time.sleep(.25)