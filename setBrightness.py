import screen_brightness_control as sbc
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()

monitors = []

def get_MonitorsAndBrightness():
    for monitor in sbc.list_monitors():
        monitors.append(str(monitor) + ": " + str(sbc.get_brightness(monitor)) + "    ")
        # print(monitor, ":", sbc.get_brightness(monitor))
    return monitors





# print(sbc.get_brightness(display=0)) #display=0 is left
# sbc.set_brightness(46, display=0)

# print(sbc.get_brightness(display=1)) #display=1 is right
# sbc.set_brightness(50, display=1)


if __name__ == "__main__":
    window()
    # get_brightness()
