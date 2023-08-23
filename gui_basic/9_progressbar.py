import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")

# progressbar.start(10)  # 10ms per frame
# progressbar.pack()


# def btncmd():
#     progressbar.stop()


# btn = Button(root, text="stop", command=btncmd)
# btn.pack()

def btncmd2():
    for i in range(1, 101):  # 1 ~ 100
        time.sleep(0.01)  # 0.01 delay

        p_var2.set(i)  # progress bar value setting
        progressbar2.update()  # ui update
        print(p_var2.get())


p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

btn = Button(root, text="start", command=btncmd2)
btn.pack()

root.mainloop()
