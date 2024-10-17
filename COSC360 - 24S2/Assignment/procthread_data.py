import matplotlib.pyplot as plt
import numpy as np
import re

# Define the parameters for children and threads
threads = [4, 8, 16]
children = [3, 6, 9, 12]
data_file = 'procthread_results.txt'

# Initialize a dictionary to store real times
real_times = {child: [] for child in children}

# Read and parse the file for real times
with open(data_file, 'r') as file:
    current_child = None
    for line in file:
        # Match the current child/thread configuration
        match_config = re.search(r'n_child = (\d+), n_thread = (\d+)', line)
        if match_config:
            current_child = int(match_config.group(1))
        
        # Find and parse the real time
        match_time = re.search(r"real\s+([\d.]+)", line)
        if match_time and current_child is not None:
            real_times[current_child].append(float(match_time.group(1)))
            current_child = None  # Reset for next configuration

print(real_times)

# Define the plot dimensions
x = np.arange(len(threads))  # Number of thread configurations
bar_width = 0.2  # Width of the bars

# Set up the figure
plt.figure(figsize=(12, 6))

# Plot each bar for the different numbers of children
for i, child in enumerate(children):
    offset_x = x + i * bar_width
    plt.bar(offset_x, real_times[child], width=bar_width, label=f'n_child = {child}')

# Add labels, title, and legend
plt.xlabel('Number of Threads')
plt.ylabel('Real Time (s)')
plt.title('Performance Comparison of Real Time by Number of Children and Threads')
plt.xticks(x + bar_width * 1.5, threads)  # Position x ticks in the center of grouped bars
plt.legend(title='Number of Children')

# Display the plot
plt.tight_layout()
plt.show()
