import pyautogui
import time

for i in range(0,100):
    locategate = pyautogui.locateOnScreen('C:/Users/ryans/OneDrive/PROGRAMMING/gamebot/Eve/autopilot/gate.PNG', confidence=.5)
    pyautogui.keyDown('d')
    pyautogui.click(locategate)
    pyautogui.keyUp('d')
    time.sleep(1)
    print(locategate)