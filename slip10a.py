# Write Python GUI program to display an alert message when a button is pressed.

from tkinter import *

import tkinter.messagebox

root = tkinter.Tk()

root.title("When you press a button the message will pop up")
root.geometry('500x300')


def onClick():
	tkinter.messagebox.showinfo("Welcome to GFG.", "Hi I'm your message")

button = Button(root, text="Click Me", command=onClick, height=5, width=10)

button.pack(side='bottom')
root.mainloop()

