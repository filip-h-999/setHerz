import pyautogui
import subprocess
import time
import keyboard
import win32api


# x, y = pyautogui.position()
# print(f"Current Cursor Position - X: {x}, Y: {y}")

# coordinatesAdvanced = X: 1165, Y: 897
# coordinatesHz = 1504, Y: 630
# coordinatesHz165 = X: 1504, Y: 528
# coordinatesHz75 = X: 1470, Y: 634 / 1493, Y: 742
# keepChanges = X: 936, Y: 613

def getHzStatus():
    device = win32api.EnumDisplayDevices(None, 0)
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    refresh_rate = settings.DisplayFrequency
    print(f"Current Refresh Rate: {refresh_rate}Hz")


def setHz(HzX, HzY):
    command = "start ms-settings:display-advanced"
    subprocess.run(["powershell", "-Command", command])

    time.sleep(1)
    pyautogui.click(1165, 897)
    time.sleep(1)
    pyautogui.click(1504, 630)
    time.sleep(1)
    pyautogui.click(HzX, HzY)
    time.sleep(3)
    pyautogui.click(936, 613)


choice = input("Whitch Herz do you want to set? : 75Hz = a or 165Hz = d?")

while choice != "a" and choice != "d" and choice != "s" and choice != "q":
        print("Please enter a valid input!")
        choice = input("Whitch Herz do you want to set? : 75Hz = a or 165Hz = d?")

if choice == "d": # 165Hz
    setHz(1504, 528)
    time.sleep(1)
    keyboard.press_and_release("alt+F4")
    exit()

elif choice == "a": # 75Hz
    setHz(1493, 742)
    time.sleep(1)
    keyboard.press_and_release("alt+F4")
    exit()

elif choice == "s":
    getHzStatus()

elif choice == "q":
    exit()