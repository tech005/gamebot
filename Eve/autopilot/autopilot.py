import pyautogui
import time

while True:
    locatestation = pyautogui.locateOnScreen('C:/Users/ryans/OneDrive/PROGRAMMING/gamebot/Eve/autopilot/station.PNG', confidence=0.8)
    locategate = pyautogui.locateOnScreen('C:/Users/ryans/OneDrive/PROGRAMMING/gamebot/Eve/autopilot/gate.PNG', confidence=0.8)
    if (locategate != None):
        print("gate found")
        pyautogui.keyDown('d')
        pyautogui.click(locategate)
        pyautogui.keyUp('d')
    elif (locatestation != None):
        print("station found")
        pyautogui.keyDown('d')
        pyautogui.click(locategate)
        pyautogui.keyUp('d')
    else:
        print("no destination found")
        break
    time.sleep(1)
