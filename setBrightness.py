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


def window():
    app.title("Brightness contro")
    app.geometry("460x277")
    app.resizable(False, False)

    name = customtkinter.CTkLabel(
        master=app, text="Brightness contro", font=("Arial", 20, "bold")
    )
    name.place(relx=0.313, rely=0.025)

    displays()
    brightness()
    text()

    nextSite()
    firstSite()
    dropdown()
    app.mainloop()


def displays():
    display = customtkinter.CTkLabel(
        master=app, text="".join(get_MonitorsAndBrightness()), font=("Arial", 13)
    )
    display.place(relx=0.10, rely=0.25)


def brightness():
    global monitor_index
    varInt = customtkinter.IntVar()
    brightness = customtkinter.CTkSlider(
        master=app,
        from_=0,
        to=100,
        orientation="horizontal",
        width=250,
        variable=varInt,
        command=lambda x: sbc.set_brightness(int(x), monitor_index),
    )
    brightness.place(relx=0.25, rely=0.50 + 0.12)

    text = customtkinter.CTkLabel(master=app, textvariable=varInt, width=30)
    text.place(relx=0.80, rely=0.48 + 0.12)


def text():
    text = customtkinter.CTkLabel(master=app, text="Brightness:", width=30)
    text.place(relx=0.10, rely=0.60)


def nextSite():
    btn = customtkinter.CTkButton(
        master=app, text=">", width=40, height=15, command=nextSite
    )
    btn.place(relx=0.86, rely=0.87)


def firstSite():
    btn = customtkinter.CTkButton(
        master=app, text="<", width=40, height=15, command=firstSite
    )
    btn.place(relx=0.75, rely=0.87)


def updateDropdownIndex(event=None):
    global monitor_index
    selected_monitor = dropdownBox.get()
    monitor_index = monitors.index(selected_monitor)
    print(monitor_index)


def dropdown():
    global dropdownBox
    dropdownBox = customtkinter.CTkComboBox(
        master=app, values=monitors, command=updateDropdownIndex
    )
    dropdownBox.place(relx=0.09, rely=0.45)


# print(sbc.get_brightness(display=0)) #display=0 is left
# sbc.set_brightness(46, display=0)

# print(sbc.get_brightness(display=1)) #display=1 is right
# sbc.set_brightness(50, display=1)


if __name__ == "__main__":
    window()
    # get_brightness()
