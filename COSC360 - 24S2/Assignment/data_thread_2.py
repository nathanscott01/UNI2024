import os
import re
import matplotlib.pyplot as plt
import numpy as np

# Path to the directory containing the .txt files
directory = "Old Data"
input_identifier = "Running ./proc_thread with input_50.txt"  # This is the line to identify before extracting the real time

# Define colors for different child process counts
colors = {
    '3': 'blue',
    '6': 'green',
    '9': 'orange',
    '12': 'red'
}

# Prepare a dictionary to store data
data = {}

# Regular expression to find 'real' time lines
real_time_pattern = re.compile(r"real (\d+\.\d+)")

# Loop through all .txt files in the directory
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        filepath = os.path.join(directory, filename)
        
        # Extract the number of children and threads from the filename
        parts = filename.replace(".txt", "").split("_")
        if len(parts) != 4:
            continue  # Skip files that don't match the naming convention
        child_count = parts[2]
        thread_count = parts[3]
        
        with open(filepath, 'r') as file:
            lines = file.readlines()
            current_real_time = None
            for i, line in enumerate(lines):
                if input_identifier in line:  # Look for specific program and input identifier
                    # Find 'real' time in the following lines
                    real_time_match = real_time_pattern.search(lines[i + 1])  # 'real' time should follow the identifier line
                    if real_time_match:
                        current_real_time = float(real_time_match.group(1))
                        break
            
            # Collect data for plotting
            if current_real_time is not None:
                if thread_count not in data:
                    data[thread_count] = {'3': [], '6': [], '9': [], '12': []}
                data[thread_count][child_count].append(current_real_time)

# Sort the thread counts for plotting
thread_counts = sorted(data.keys(), key=lambda x: int(x))

# Plotting
x = np.arange(len(thread_counts))  # The x locations for the groups
width = 0.2  # The width of the bars
offsets = [-1.5, -0.5, 0.5, 1.5]  # Positions for each child count's bar

fig, ax = plt.subplots(figsize=(12, 8))

# For each child process count, plot its corresponding bars
for idx, child_count in enumerate(['3', '6', '9', '12']):
    y_values = [np.mean(data[thread][child_count]) for thread in thread_counts]
    ax.bar(x + offsets[idx] * width, y_values, width, label=f"{child_count} child processes", color=colors[child_count])

# Labeling and formatting
ax.set_xlabel('Thread Count')
ax.set_ylabel('Real Time (seconds)')
ax.set_title('Real Time for Different Thread and Child Process Counts')
ax.set_xticks(x)
ax.set_xticklabels(thread_counts)
ax.legend(title="Child Processes")
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
