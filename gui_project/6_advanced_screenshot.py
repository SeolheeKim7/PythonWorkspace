import time
import keyboard
from PIL import ImageGrab


def screenshot():
    # take screenshot
    curr_time = time.strftime("%Y%m%d%H%M%S")
    img = ImageGrab.grab()
    # save screenshot as image1.png, image2.png, ...
    # save with current time
    img.save("image{}.png".format(curr_time))


keyboard.add_hotkey("F9", screenshot)  # press F9 to take screenshot
# keyboard.add_hotkey("a", screenshot)  # press a to take screenshot
# keyboard.add_hotkey("ctrl+shift+s", screenshot)  # press ctrl+shift+s to take screenshot
# press ESC to quit
keyboard.wait("esc")
