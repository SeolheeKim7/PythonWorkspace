import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("SH GUI")
root.geometry("640x480")  # width * height

# assume this is a app for train ticket reservation


def info():
    msgbox.showinfo("info", "Your seat is booked successfully")


def warn():
    msgbox.showwarning("warning", "This seat is already booked")


def error():
    msgbox.showerror("error", "Payment failed")


def okcancel():
    response = msgbox.askokcancel(
        "ok / cancel", "Do you want to book this seat?")
    print("response: ", response)
    if response == 1:
        print("ok")
    elif response == 0:
        print("cancel")


def retrycancel():
    msgbox.askretrycancel(
        "retry / cancel", "Do you want to book this seat again?")


def yesno():
    msgbox.askyesno("yes / no", "Do you want to book this seat?")


def yesnocancel():
    response = msgbox.askyesnocancel(
        title=None, message="Do you want to book this seat?")
    # yes: save and close
    # no: close without saving
    # cancel: cancel
    # True, False, None -> Yes: 1, No: 0, Cancel: others
    print("response: ", response)
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")


Button(root, command=info, text="info").pack()
Button(root, command=warn, text="warn").pack()
Button(root, command=error, text="error").pack()
Button(root, command=okcancel, text="okorcancel").pack()
Button(root, command=retrycancel, text="retry").pack()
Button(root, command=yesno, text="yes no").pack()
Button(root, command=yesnocancel, text="yes no cancel").pack()


root.mainloop()
