from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

label1 = Label(root, text="Choose the menu").pack()

burger_var = IntVar()  # chkvar has int type
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="chickenHamburger",
                          value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="cheeseHamburger",
                          value=3, variable=burger_var)
btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Choose the drink").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="Coke", value="coke", variable=drink_var)
btn_drink1.select()  # default value
btn_drink2 = Radiobutton(root, text="Cider", value="cider", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()


def btncmd():
    print(burger_var.get())  # selected radio button's value
    print(drink_var.get())


btn = Button(root, text="Order", command=btncmd)
btn.pack()
root.mainloop()
