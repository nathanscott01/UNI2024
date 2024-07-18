"""
Nathan Scott
COSC368 Lab 1
Scrolling Window
"""

from tkinter import *
from tkinter.ttk import *

# Build window 24x 10y
window = Tk()
# window.geometry("24x10")

vy = Scrollbar(window, orient='vertical')
vy.pack(side=RIGHT, fill='y')
vx = Scrollbar(window, orient='horizontal')
vx.pack(side=BOTTOM, fill='x')

# Frame to hold text
text_frame = Text(window, wrap=NONE, width = 24, height=10,
                  font="helvetica 12", xscrollcommand=vx.set, 
                  yscrollcommand=vy.set)

# Insert text
# example = "The quick brown fox jumps over the lazy dog"
example = ("Lorem Ipsum is simply dummy text of the \n"
           "printing and typesetting industry. \n"
           "Lorem Ipsum has been the industry's \n"
           "standard dummy text ever since the 1500s, \n"
           "when an unknown printer took a galley of \n"
           "type and scrambled it to make a type specimen book. \n"
           "It has survived not only five centuries, \n"
           "but also the leap into electronic typesetting, \n"
           "remaining essentially unchanged. It was \n"
           "popularised in the 1960s with the release \n"
           "of Letraset sheets \n"
           "containing Lorem Ipsum passages, and more \n"
           "recently with desktop publishing software \n"
           "like Aldus PageMaker \n"
           "including versions of Lorem Ipsum.\n")
text_frame.insert(END, example)

text_frame.pack()

vx.config(command=text_frame.xview)
vy.config(command=text_frame.yview)
window.mainloop()
