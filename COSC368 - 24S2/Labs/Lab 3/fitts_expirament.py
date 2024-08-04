"""
Nathan Scott
COSC368 Lab 3
Fitts Experiment
"""

from tkinter import *
from tkinter.ttk import *
import random
import time
import csv

master = Tk()
c = Canvas(master, width=600, height=200)
c.pack()

# Test Parameters
distances = [64, 128, 256, 512]
widths = [8, 16, 32]
combinations = [(d, w) for d in distances for w in widths]
repitions = 4
name = StringVar()
log = []

def choose_random():
    """Choose a random (d, w) tuple from set and remove"""
    test_tuple = random.choice(combinations)
    combinations.remove(test_tuple)
    return test_tuple

def test_set(test_tuple):
    """Run n repitions for the set, and log times"""
    start_time = None
    distance, width = test_tuple
    n = 0
    
    def record_time():
        nonlocal start_time, n
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        duration = f"{duration:.2f}"
        log_entry = [name.get(), distance, width, n, duration]
        log.append(log_entry)
        n += 1
        run_current_test()
    
    def check_left(event):
        nonlocal n
        if n % 2 == 1:
            record_time()
            
    def check_right(event):
        nonlocal n
        if n % 2 == 0:
            record_time()
            
    def run_current_test():
        nonlocal n, start_time
        if n < repitions:
            c.delete("all")
            start_time = time.time()
            rect1 = c.create_rectangle((600 - distance - width) / 2, 0, (600 - distance + width) / 2, 200, tag="left")
            rect2 = c.create_rectangle((600 + distance - width) / 2, 0, (600 + distance + width) / 2, 200, tag="right")
            
            if n % 2 == 0:
                c.itemconfigure(rect1, fill="blue")
                c.itemconfigure(rect2, fill="green")
            else:
                c.itemconfigure(rect1, fill="green")
                c.itemconfigure(rect2, fill="blue")
                
            c.tag_bind(rect1, "<Button-1>", check_left)
            c.tag_bind(rect2, "<Button-1>", check_right)
            
        else:
            run_tests()
        
    # Call the next test_set
    run_current_test()
    
def write_log_to_csv(log):
    with open('fitts_tests.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Distance", "Width", "Block Count", "Time Taken"])
        writer.writerows(log)

def run_tests():
    """Run the tests"""
    if combinations:
        test_tuple = choose_random()    # Choose a random tuple
        test_set(test_tuple)            # Run tests for the tuple
    else:
        text_output.set("Finished!")
        write_log_to_csv(log)

def start_experiment():
    """Start the experiment after getting the user's name"""
    name.set(name_entry.get())
    name_frame.pack_forget()
    run_tests()

# Setup initial frame to capture the user's name
name_frame = Frame(master)
name_frame.pack(pady=20)

Label(name_frame, text="Enter your name:").pack(side=LEFT)
name_entry = Entry(name_frame, textvariable=name)
name_entry.pack(side=LEFT)
Button(name_frame, text="Start", command=start_experiment).pack(side=LEFT)

# Format the top section for displaying status messages
text_output = StringVar()
text_output.set("")
input_text = Label(master, textvariable=text_output)
input_text.pack()

master.mainloop()        