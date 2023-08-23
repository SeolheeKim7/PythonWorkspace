from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

# selectmode: single, extended, height: 0 means all
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "Apple")
listbox.insert(1, "Strawberry")
listbox.insert(2, "Banana")
listbox.insert(END, "Watermelon")
listbox.insert(END, "Grape")
listbox.pack()


def btncmd():
    # delete
    # listbox.delete(END)  # delete the last item
    # count
    # print("The number of items: ", listbox.size())

    # check
    # print("1st to 3rd items: ", listbox.get(0, 2))

    # check selected item
    print("Selected item: ", listbox.curselection())


btn = Button(root, text="Click", command=btncmd)
btn.pack()
root.mainloop()
