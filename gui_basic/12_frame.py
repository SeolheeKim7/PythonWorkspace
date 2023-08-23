from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height


Label(root, text="Choose your menu").pack(side="top")

Button(root, text="Order").pack(side="bottom")

# Frame: a widget that groups other widgets
frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheeseburger").pack()
Button(frame_burger, text="Chickenburger").pack()

# Drink frame
frame_drink = LabelFrame(root, text="Drink")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="Coke").pack()
Button(frame_drink, text="Sprite").pack()

root.mainloop()
