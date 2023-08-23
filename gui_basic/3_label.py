from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

label1 = Label(root, text="Hello World")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()


def change():
    label1.config(text="See you again")

    global photo2
    photo2 = PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)


btn = Button(root, text="Click me", command=change)
btn.pack()
root.mainloop()
