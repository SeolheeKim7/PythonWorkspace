from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "Input text")

e = Entry(root, width=30)  # single line
e.pack()
e.insert(0, "Single line")


def btncmd():
    # print(txt.get("1.0", END))  # 1: line 1, 0: column 0
    # print(e.get())
    print(txt.get("1.0", END))  # 1: line 1, 0: column 0
    print(e.get())

    txt.delete("1.0", END)
    e.delete(0, END)


btn = Button(root, text="Click", command=btncmd)
btn.pack()
root.mainloop()
