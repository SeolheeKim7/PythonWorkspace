import time
from PIL import ImageGrab

time.sleep(5)  # wait 5 seconds

for i in range(1, 11):  # take 10 screenshots in every 2seconds
    img = ImageGrab.grab()  # take screenshot
    # save screenshot as image1.png, image2.png, ...
    img.save("image{}.png".format(i))
    time.sleep(2)  # wait 2 seconds
