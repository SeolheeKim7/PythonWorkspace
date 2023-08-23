from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

chkvar = IntVar()  # chkvar has int type
chkbox = Checkbutton(
    root, text="Do not show this message for today", variable=chkvar)
# chkbox.select() # select the checkbox
# chkbox.deselect() # deselect the checkbox
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(
    root, text="Do not show this message for today, too", variable=chkvar2)
chkbox2.pack()


def btncmd():
    print(chkvar.get())  # 0: unchecked, 1: checked
    print(chkvar2.get())


btn = Button(root, text="Click", command=btncmd)
btn.pack()
root.mainloop()
