"""
Nathan Scott
COSC368 Lab 2
Keyboard Expirament GUI
"""

from tkinter import *
import random
import time
import csv

# Build Window
window = Tk()

target = "qwertyuiop"   # Target letters
n = 6  # Number of blocks
num_letters_per_block = 6  # Number of letters per block
letter_set = []  # To store the current set of letters for a block
start_time = None
log = []
dynamic = False

name = "Geoffrey"
condition = "static"

# Define insert and clear functions
def check_char(current_char, key_value):
    global start_time
    if current_char.get() == key_value:
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        duration = f"{duration:.2f}"
        block_count = n + 1
        log_entry = [name, condition, key_value, block_count, duration]
        log.append(log_entry)
        if letter_set:
            choose_and_display_random_letter()
        else:
            start_block()

def choose_and_display_random_letter():
    global start_time
    letter = random.choice(letter_set)
    letter_set.remove(letter)
    test_user.set(letter)
    start_time = time.time()

def choose_random(target_letters, num_letters):
    random_letters = random.sample(target_letters, num_letters)
    return random_letters

def start_block():
    global n, letter_set
    if n > 0:
        test_user.set(f"Block {n}")
        window.after(2000, run_block)
    else:
        test_user.set("Finished!!")
        write_log_to_csv(log)
        
def run_block():
    global n, letter_set
    letter_set = choose_random(target, num_letters_per_block)
    n -= 1
    choose_and_display_random_letter()

def write_log_to_csv(log):
    with open('keyboard_log.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Condition", "Target Character", "Block Count", "Time Taken"])
        writer.writerows(log)
        

# Create table separating keyboard from output and clear button
frame_top = Frame(window)
frame_top.pack(side=TOP, padx=10, pady=10, fill=X)
frame_bottom = Frame(window, borderwidth=2, relief=RAISED)
frame_bottom.pack(side=BOTTOM, padx=5, pady=5)

# Format the top section

test_user = StringVar()
test_user.set("")
input_text = Label(frame_top, textvariable=test_user)
input_text.pack()

# Assemble Keyboard
board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

# Create Test
for i in range(len(board)):
    row_frame = Frame(frame_bottom)
    for j in range(len(board[i])):
        key_value = board[i][j]
        button_frame = Frame(row_frame, height=64, width=64)
        button_frame.pack(side=LEFT)
        button = Button(button_frame, text=key_value)
        button.bind("<Button-1>", lambda event, key=key_value: check_char(test_user, key))
        button.pack()
    row_frame.grid(row=i)
    
# Display the first random letter
start_block()

# Call window main loop
window.mainloop()
