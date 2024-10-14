import matplotlib.pyplot as plt
import numpy as np
import re
import os

# Define file paths and configurations
directory = 'Old Data'
threads = [4, 8, 12, 16]
children = [3, 6, 9, 12]
num_cases = len(children)

# Initialize dictionary to store results
results = {t: [] for t in threads}

# Read each file and extract real times
for filename in os.listdir(directory):
    # Extract number of children and threads from the filename
    match = re.search(r'proc_thread_result_(\d+)_(\d+)\.txt', filename)
    if match:
        n_child = int(match.group(1))
        n_thread = int(match.group(2))

        # Ensure we only process files matching our children and threads lists
        if n_thread in threads and n_child in children:
            with open(os.path.join(directory, filename), 'r') as file:
                # Extract the real time for input_50.txt
                for line in file:
                    real_time_match = re.search(r"real\s+([\d.]+)", line)
                    if real_time_match:
                        real_time = float(real_time_match.group(1))
                        results[n_thread].append(real_time)
                        break  # Only take the first 'real' time encountered for input_50.txt

# Plotting
x = np.arange(len(threads))  # the label locations
width = 0.2  # the width of the bars

# Define figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot data for each number of children
for i, child in enumerate(children):
    real_times_for_child = [results[t][i] for t in threads]  # Extract the real times for each thread setting
    ax.bar(x + i * width, real_times_for_child, width, label=f'n_child = {child}')

# Add labels, title, and legend
ax.set_xlabel('Number of Threads')
ax.set_ylabel('Real Time (s)')
ax.set_title('Real Time for Different Numbers of Threads and Children')
ax.set_xticks(x + width * 1.5)
ax.set_xticklabels(threads)
ax.legend(title='Number of Children')

# Show plot
plt.tight_layout()
plt.show()
