import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("SH GUI")
# root.geometry("640x480+300+100") # width * height + x  + y

# file frame (file add, delete)
file_frame = Frame(root)
# fill="x" means fill the whole space
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="Add File")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="Delete File")
btn_del_file.pack(side="right")

# list frame

list_frame = Frame(root)
list_frame.pack(fill="both")  # fill="both" means fill the whole space

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended",
                    height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# save path frame
path_frame = LabelFrame(root, text="Save Path")
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)  # ipady: inner padding

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True,
                   ipady=4)  # change height of the input box

btn_dest_path = Button(path_frame, text="Find", width=10)

btn_dest_path.pack(side="right", padx=5, pady=5)

# option frame
frame_option = LabelFrame(root, text="Option")
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. width option
# width label
lbl_width = Label(frame_option, text="Width", width=8)
lbl_width.pack(side="left", padx=5, pady=5)

# width combo
opt_width = ["Original", "1024", "800", "640"]
cmb_width = ttk.Combobox(frame_option, state="readonly",
                         values=opt_width, width=10)
cmb_width.current(0)  # set the first option as default
cmb_width.pack(side="left", padx=5, pady=5)

# 2. space option
# width label
lbl_space = Label(frame_option, text="Space", width=8)
lbl_space.pack(side="left", padx=5, pady=5)

# width combo
opt_space = ["None", "Narrow", "Normal", "Wide"]
cmb_space = ttk.Combobox(frame_option, state="readonly",
                         values=opt_space, width=10)
cmb_space.current(0)  # set the first option as default
cmb_space.pack(side="left", padx=5, pady=5)

# 3. file format option
# width label
lbl_format = Label(frame_option, text="Format", width=8)
lbl_format.pack(side="left", padx=5, pady=5)

# width combo
opt_format = ["PNG", "JPG", "BMP"]
cmb_format = ttk.Combobox(frame_option, state="readonly",
                          values=opt_format, width=10)
cmb_format.current(0)  # set the first option as default
cmb_format.pack(side="left", padx=5, pady=5)

# progress bar
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill="x", padx=5, pady=5)

# run frame
frame_run = Frame(root)
frame_run.pack(fill="x", padx=5, pady=5)

# close button
btn_close = Button(frame_run, padx=5, pady=5, text="Close",
                   width=12, command=root.quit)
btn_close.pack(side="right", padx=5, pady=5)

# start button
btn_start = Button(frame_run, padx=5, pady=5, text="Start", width=12)
btn_start.pack(side="right", padx=5, pady=5)


# run button


root.resizable(False, False)  # x(width), y(height) value cannot be changed
root.mainloop()
