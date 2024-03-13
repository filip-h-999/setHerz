import pyautogui
import subprocess
import time
import keyboard
import win32api
import win32con

# x, y = pyautogui.position()
# print(f"Current Cursor Position - X: {x}, Y: {y}")

# coordinatesAdvanced = X: 1165, Y: 897
# coordinatesHz = 1504, Y: 630
# coordinatesHz165 = X: 1504, Y: 528
# coordinatesHz75 = X: 1470, Y: 634 / 1493, Y: 742
# keepChanges = X: 936, Y: 613

deviceName = r"\\.\DISPLAY2"

def getHzStatus():
    settings = win32api.EnumDisplaySettings(deviceName, -1)
    refresh_rate = settings.DisplayFrequency
    print(f"Current Refresh Rate: {refresh_rate}Hz")


def setHz02(refresh_rate):
    # device = win32api.EnumDisplayDevices(None, 0)
    # print(device.DeviceName)
    # if device.DeviceName:
    devmode = win32api.EnumDisplaySettings(deviceName, win32con.ENUM_CURRENT_SETTINGS)
    devmode.DisplayFrequency = refresh_rate
    result = win32api.ChangeDisplaySettingsEx(deviceName, devmode)
    
    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print("Display refresh rate changed successfully.")
    else:
        print("Failed to change display refresh rate.")
    # else:
    #     print("No valid display device found.")


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


while True:
    choice = input("Whitch Herz do you want to set? : 75Hz = a or 165Hz = d?")
    if choice == "d":  # 165Hz
        # setHz(1504, 528)
        # time.sleep(1)
        # keyboard.press_and_release("alt+F4")
        setHz02(165)

    elif choice == "a":  # 75Hz
        # setHz(1493, 742)
        # time.sleep(1)
        # keyboard.press_and_release("alt+F4")
        setHz02(75)

    elif choice == "s":
        getHzStatus()

    elif choice == "q":
        exit()

    else:
        print("Please enter a valid input! (a or d) or (s) or (q)")
        continue
