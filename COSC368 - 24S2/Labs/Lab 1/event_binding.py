"""
Nathan Scott
COSC368 Lab 1
Event Binding
"""

from tkinter import *
from tkinter.ttk import *

def add_one():
    value.set(value.get()+1)
    
def wow(event):
    label2.config(text="WWWWWOOOOWWWW")
    
window = Tk()

value = IntVar(window, 0)

label = Label(window, textvariable=value)
label.pack()
label2 = Label(window)
label2.pack()

button = Button(window, text="Add one", command=add_one)
button.bind("<Shift-Double-Button-1>", wow)
button.pack()

window.mainloop()
