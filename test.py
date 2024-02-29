import pygetwindow as gw

def get_window_position_and_size(window_title):
    window = gw.getWindowsWithTitle(window_title)[0]
    position = window.left, window.top
    size = window.width, window.height
    return position, size

window_title_to_find = "discord"
result = get_window_position_and_size(window_title_to_find)

if result is not None:
    position, size = result
    print(f"Position: {position}")
    print(f"Size: {size}")
