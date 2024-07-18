"""
Nathan Scott
COSC368 Lab 1
Question 2
"""

from tkinter import *
from tkinter.ttk import *

window = Tk()


# side_labels = ["bottom1", "bottom2", "top1", "top2", "left1", "right1"]
# for theside in side_labels:
#     button = Button(window, text=theside)
#     button.pack(side=theside[0:-1])
    
# for label_num in range(6):
#     button = Button(window, text="Button"+str(label_num))
#     button.grid(row=label_num // 3, column=label_num % 3)

for label_num in range(6):
    button = Button(window, text="Button"+str(label_num))
    button.grid(row=label_num // 2, column=label_num % 3)
    if label_num==1:
        button.grid(columnspan=2, sticky="ew")
    elif label_num == 3:
        button.grid(rowspan=2, sticky="ns")
window.columnconfigure(1, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

window.mainloop()