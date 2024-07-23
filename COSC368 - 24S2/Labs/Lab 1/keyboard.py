"""
Nathan Scott
COSC368 Lab 1
Keyboard GUI
"""

from tkinter import *

# Build Window
window = Tk()

# Define insert and clear functions
def clear_all():
    user_input.set("")
    
def insert_char(current_string, key_value):
    user_input.set(current_string.get() + key_value)

# Create table separating keyboard from output and clear button
frame_top = Frame(window)
frame_top.pack(side=TOP, padx=10, pady=10, fill=X)
frame_bottom = Frame(window, borderwidth=2, relief=RAISED)
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
button_size = 4

for i in range(len(board)):
    row_frame = Frame(frame_bottom)
    for j in range(len(board[i])):
        key_value = board[i][j]
        button = Button(row_frame, text=key_value, width=button_size, relief=RAISED)
        button.bind("<Button-1>", lambda event, key=key_value: insert_char(user_input, key))
        button.pack(side=RIGHT)
    row_frame.grid(row=i)

# Call window main loop


window.mainloop()