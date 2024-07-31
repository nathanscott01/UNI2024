"""
Nathan Scott
COSC368 Lab 2
Keyboard Experiment + Static/Dynamic Functionality
"""

from tkinter import *
import random
import time
import csv


window = Tk()
window.minsize(300, 200)

# Globals
name = StringVar()
dynamic = BooleanVar()

target = "qwertyuiop"   # Target letters
n = 6  # Number of blocks
num_letters_per_block = 6  # Number of letters per block
letter_set = []  # To store the current set of letters for a block
start_time = None
log = []


# Name + Mode Setup
def test_setup():

    def record_username():
        name.set(user_entry_name.get())
        name_entry_frame.pack_forget()
        ask_for_mode()
        
    def ask_for_mode():
        text_output.set("Select test mode below")
        mode_frame.pack()
        
    def set_mode(chosen_mode):
        dynamic.set(chosen_mode == "Dynamic")
        mode_frame.pack_forget()
        frame_bottom.pack_forget()
        text_output.set(f"Name: {name.get()}, Mode: {'Dynamic' if dynamic.get() else 'Static'}")
        window.after(1000, run_test)

    text_output.set("Enter your name below")

    # Create a frame for name entry
    name_entry_frame = Frame(frame_bottom)
    name_entry_frame.pack()
    
    # Setup text input window in bottom frame for input
    user_entry_name = Entry(name_entry_frame, textvariable=name)
    user_entry_name.grid(row=0)
    
    # Needs an enter button below
    enter_button = Button(name_entry_frame, text="Enter", command=record_username)
    enter_button.grid(row=1)
    
    # Create a frame for mode selection
    mode_frame = Frame(frame_bottom)
    mode_frame.pack_forget()  # Initially hide the mode frame
    
    # Setup mode buttons
    button_static = Button(mode_frame, text="Static", command=lambda: set_mode("Static"))
    button_static.grid(row=0, column=0)
    button_dynamic = Button(mode_frame, text="Dynamic", command=lambda: set_mode("Dynamic"))
    button_dynamic.grid(row=0, column=1)
    
    
# Run Keyboard Tests
def run_test():
    
    global letter_set, n, num_letters_per_block, target, start_time, log, text_output, dynamic, name
    
    if not dynamic.get():
        condition = "static"
    else:
        condition = "dynamic"
        
    def check_char(selected_key):
        global start_time
        if text_output.get() == selected_key:
            end_time = time.time()
            duration = (end_time - start_time) * 1000
            duration = f"{duration:.2f}"
            block_count = n + 1
            log_entry = [name.get(), condition, selected_key, block_count, duration]
            log.append(log_entry)
            if letter_set:
                choose_and_display_random_letter()
            else:
                start_block()

    def choose_and_display_random_letter():
        global start_time
        letter = random.choice(letter_set)
        letter_set.remove(letter)
        text_output.set(letter)
        start_time = time.time()

    def choose_random(target_letters, num_letters):
        random_letters = random.sample(target_letters, num_letters)
        return random_letters

    def start_block():
        global n, letter_set
        if n > 0:
            text_output.set(f"Block {7 - n}")
            if dynamic.get():
                assemble_keyboard()
            window.after(1000, run_block)
        else:
            text_output.set("Finished!!")
            write_log_to_csv(log, dynamic.get())
            
    def run_block():
        global n, letter_set
        letter_set = choose_random(target, num_letters_per_block)
        n -= 1
        choose_and_display_random_letter()

    def write_log_to_csv(log, mode_status):
        if not mode_status:
            with open('experiment_static_log.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Condition", "Target Character", "Block Count", "Time Taken"])
                writer.writerows(log)
        else:
            with open('experiment_dynamic_log.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Condition", "Target Character", "Block Count", "Time Taken"])
                writer.writerows(log)
            
    def assemble_keyboard():
        frame_bottom.pack(side=BOTTOM, padx=5, pady=5)\
        # Shuffle the alphabet
        alphabet = list('qwertyuiopasdfghjklzxcvbnm')
        random.shuffle(alphabet)
        board = [alphabet[:10], alphabet[10:19], alphabet[19:]]
        for widget in frame_bottom.winfo_children():
            widget.destroy()             
        # Create Keyboard
        for i in range(len(board)):
            row_frame = Frame(frame_bottom)
            for j in range(len(board[i])):
                key_value = board[i][j]
                button_frame = Frame(row_frame, height=64, width=64)
                button_frame.pack(side=LEFT)
                button = Button(button_frame, text=key_value)
                button.bind("<Button-1>", lambda event, key=key_value: check_char(key))
                button.pack()
            row_frame.grid(row=i)
            
    if not dynamic.get():
        assemble_keyboard()
    start_block()
    

# Setup Frames
frame_top = Frame(window)
frame_top.pack(side=TOP, padx=10, pady=10, fill=X)
frame_bottom = Frame(window, borderwidth=2, relief=RAISED)
frame_bottom.pack(side=BOTTOM, padx=5, pady=5)

# Format the top section
text_output = StringVar()
text_output.set("")
input_text = Label(frame_top, textvariable=text_output)
input_text.pack()

test_setup()

# Call window main loop
window.mainloop()
