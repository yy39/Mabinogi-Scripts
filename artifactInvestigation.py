# Cooldown for Artifact Investigation is 180s from rank N to B, 120s from rank A to 8, 60s from 7 to 4, and 30s from 3 to 1
# could also use open-cv to determine when Artifact Investigation is off cooldown, but seems a bit more intensive

# click on skill
# window opens prompting to select an item
# select item via leftclick
# left click ok
# yet another window prompt asking to confim
# left click ok
# wait for number of sec depending on skill rank
# this process is the same for both artifact appraisal and restoration, with slightly different window prompts
import time
import pyautogui
import config
import autoMouse

def determineSleep(rank):
    match rank:
        case '1' | '2' | '3' :
            return 30
        case '4' | '5' | '6' | '7':
            return 60
        case '8' | '9' | 'A':
            return 120
        case default:
            return 180

#may need to download all possible artifact pngs
def clickOnArtifacts(image):
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
        autoMouse.clickImage(image, retryCount)
    else:
        print(f'image found: {image}')
        retryCount = 0
        autoMouse.clickAt(imageCoords[0], imageCoords[1])

# Select Mabinogi window
autoMouse.clickMainCenter()
autoMouse.clickImage('images/artifactInvestigationIcon.png')
#sleep = determineSleep()