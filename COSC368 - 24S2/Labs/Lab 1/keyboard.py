"""
Nathan Scott
COSC368 Lab 1
Keyboard GUI
"""

from tkinter import *
from tkinter.ttk import *

# Build Window
window = Tk()

# Define insert and clear functions
def clear_all():
    user_input = ""

# Create table separating keyboard from output and clear button
frame_top = Frame(window)
frame_top.pack(side=TOP)
frame_bottom = Frame(window, borderwidth=4, relief=RIDGE)
frame_bottom.pack(side=BOTTOM, padx=5, pady=5)

# Format the top section

user_input = StringVar()
user_input.set("")
input_text = Label(frame_top, textvariable=user_input)
input_text.pack(side=LEFT)

button = Button(frame_top, text="Clear", command=clear_all)
button.pack(side=RIGHT)

# Assemble Keyboard + bind a function
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
for i in range(len(board)):
    for j in range(len(board[i])):
        button = Button(frame_bottom, text=board[i][j])
        button.grid(row=i, column=j)

# Call window main loop


window.mainloop()