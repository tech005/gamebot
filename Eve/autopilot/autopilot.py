import pyautogui
import time
import os

workingpath = os.getcwd()
stationpng = workingpath+'\Eve\\autopilot\station.PNG'
gatepng = workingpath+'\Eve\\autopilot\gate.PNG'

def autopilot(stationpng,gatepng):
    while True:
        locatestation = pyautogui.locateOnScreen(stationpng, confidence=0.8)
        locategate = pyautogui.locateOnScreen(gatepng, confidence=0.8)
        if (locategate != None):
            print("gate found")
            pyautogui.keyDown('d')
            pyautogui.click(locategate)
            pyautogui.keyUp('d')
            time.sleep(1)
        elif (locatestation != None):
            print("station found")
            pyautogui.keyDown('d')
            pyautogui.click(locatestation)
            pyautogui.keyUp('d')
            time.sleep(1)
        else:
            print("no destination found have you arrived?")
            time.sleep(5)


autopilot(stationpng,gatepng)