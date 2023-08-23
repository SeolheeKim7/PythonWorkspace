from tkinter import *

root = Tk()
root.title("SH GUI")

btn1 = Button(root, text="Button1")
btn1.pack()

btn2 = Button(root, padx=5, pady=10, text="Button2")  # set padding
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="Button3")  # set padding
btn3.pack()

btn4 = Button(root, width=10, height=3, text="Button4")  # set size
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="Button5")  # set color
btn5.pack()

photo = PhotoImage(file="gui_basic/img.png")
btn6 = Button(root, image=photo)  # set image
btn6.pack()


def btncmd():
    print("Button is clicked")


btn7 = Button(root, text="Active Button", command=btncmd)   # set event
btn7.pack()

root.mainloop()
