import pyautogui
import subprocess
import time


# x, y = pyautogui.position()
# print(f"Current Cursor Position - X: {x}, Y: {y}")

# coordinatesAdvanced = X: 1165, Y: 897
#coordinatesHz = 1504, Y: 630
#coordinatesHz165 = X: 1504, Y: 528
#coordinatesHz75 = X: 1470, Y: 634 / 1493, Y: 742
#keepChanges = X: 936, Y: 613

def setHz(HzX, HzY):
    command = 'start ms-settings:display-advanced'
    subprocess.run(['powershell', '-Command', command])
    
    time.sleep(1)
    pyautogui.click(1165, 897)
    time.sleep(1)
    pyautogui.click(1504, 630)
    time.sleep(1)
    pyautogui.click(HzX, HzY)
    time.sleep(3)
    pyautogui.click(936, 613)

choice = input("Whitch Herz do you want to set? : 75Hz = 2 or 165Hz = 1?")

if choice == "1":
    setHz(1504, 528)    
elif choice == "2":
    setHz(1493,742)
else:
    print(f"Please enter a valid number (1 or 2)")
    exit()
