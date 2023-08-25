# Quiz? use tkinter to create a program that meets the following requirements.

# [GUI Layout]
# 1. The title of the program is "Window Memo".
# 2. Menu bar is created with "File", "Edit", "Format", "View", "Help".
# 3. "File" menu has "Open File", "Save", "Exit".
# 3-1. "Open File" : open file content mynote.txt and display it on the screen.
# 3-2. "Save" : save the content of the screen to mynote.txt.
# 3-3. "Exit" : exit the program.
# 4. when the program starts, the file is empty
# 5. No need status bar.
# 6. The size of the program is adustable.
# 7. add Scrollbar to the right side of the screen.
import os
from tkinter import *

root = Tk()
root.title("Window Memo")
root.geometry("640x480")  # width * height
# root.geometry("640x480+300+100") # width * height + x  + y

# same file in the same folder named mynote.txt

# if mynote.txt exists, open it and display it on the screen
# if mynote.txt does not exist, create it and save it


def open_file():
    if os.path.isfile("mynote.txt"):
        with open("mynote.txt", "r", encoding="utf8") as file:
            txt.delete("1.0", END)
            txt.insert(END, file.read())
    # with open("mynote.txt", "r", encoding="utf8") as file:
    #     txt.delete("1.0", END)
    #     txt.insert(END, file.read())


def save_file():
    with open("mynote.txt", "w", encoding="utf8") as file:
        file.write(txt.get("1.0", END))


menu = Menu(root)

# File menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open...", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)

menu.add_cascade(label="File", menu=menu_file)

# Edit menu (empty)
menu.add_cascade(label="Edit")

# Format menu
menu.add_cascade(label="Format")

# View menu (check button)
menu.add_cascade(label="View")

# Help menu
menu.add_cascade(label="Help")
# root.resizable(False, False)  # x(width), y(height) value cannot be changed

scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# txt = Text(root, width=640, height=480)
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)
scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()
