import os
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
# import all from tkinter module (tkinter module has all the functions for GUI)
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("SH GUI")
# root.geometry("640x480+300+100") # width * height + x  + y

# add file


def add_file():
    files = filedialog.askopenfilenames(title="Select image file",
                                        filetypes=(("PNG file", "*.png"),
                                                   ("All files", "*.*")),
                                        initialdir=r"C:\PythonWorkspace")  # return file path(s)
    # user selected file list
    for file in files:
        list_file.insert(END, file)

# delete file


def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# save path (folder)


def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':  # if user cancels
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)

# merge images


def merge_image():
    # print("width: ", cmb_width.get())
    # print("space: ", cmb_space.get())
    # print("format: ", cmb_format.get())
    try:
        # wifth option
        img_width = cmb_width.get()
        if img_width == "Original":
            img_width = -1
        else:
            img_width = int(img_width)

        # space option
        img_space = cmb_space.get()
        if img_space == "Narrow":
            img_space = 30
        elif img_space == "Normal":
            img_space = 60
        elif img_space == "Wide":
            img_space = 90
        else:  # None
            img_space = 0

        # format option
        img_format = cmb_format.get().lower()  # PNG, JPG, BMP -> png, jpg, bmp

        ############################################

        # print(list_file.get(0, END))  # get all the file paths in the list
        images = [Image.open(x) for x in list_file.get(0, END)]

        # image size adjustment
        image_sizes = []  # [(width1, height1), (width2, height2), ...]
        if img_width > -1:
            # width value is set
            image_sizes = [(int(img_width), int(
                img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # width value is not set
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # [(10, 10), (20, 20), (30, 30)] -> [10, 20, 30]
        widths, heights = zip(*(image_sizes))  # *: unpacking

        # get the max width, total height
        max_width, total_height = max(widths), sum(heights)

        # create a sketchbook
        if img_space > 0:  # if space option is set
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height),
                               (255, 255, 255))  # white background
        y_offset = 0  # y position
        # for img in images:
        #     result_img.paste(img, (0, y_offset))
        #     y_offset += img.size[1]  # add the height of the image

        # progress bar
        for idx, img in enumerate(images):
            # image size adjustment
            if img_width > -1:
                # width value is set
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            # add the height of the image
            y_offset += (img.size[1] + img_space)

            progress = (idx + 1) / len(images) * 100  # calculate the progress
            p_var.set(progress)
            progress_bar.update()

        # format option
        file_name = "SH_photo." + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("Info", "Successfully merged")

    except Exception as err:  # if error occurs
        msgbox.showerror("Error", err)

# start


def start():
    # check if the value is valid
    # print("width: ", cmb_width.get())
    # print("space: ", cmb_space.get())
    # print("format: ", cmb_format.get())

    # check if the file list is empty
    if list_file.size() == 0:
        msgbox.showwarning("Warning", "Add image file(s)")
        return

    # check if the save path is empty
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning", "Select save path")
        return

    # merge images
    merge_image()


# file frame (file add, delete)
file_frame = Frame(root)
# fill="x" means fill the whole space
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12,
                      text="Add File", command=add_file)
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12,
                      text="Delete File", command=del_file)
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

btn_dest_path = Button(path_frame, text="Find",
                       width=10, command=browse_dest_path)

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
btn_start = Button(frame_run, padx=5, pady=5,
                   text="Start", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)


# run button


root.resizable(False, False)  # x(width), y(height) value cannot be changed
root.mainloop()
