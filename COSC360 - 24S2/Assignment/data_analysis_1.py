import matplotlib.pyplot as plt
import re

# Define input sizes and programs
input_sizes = [10, 20, 30, 40, 50]
programs = ['serial', 'thread', 'process', 'proc_thread']

# Initialize dictionary to hold real times for each program and input size
real_times = {program: [] for program in programs}

# Read and parse the file
with open('results_12_16.txt', 'r') as file:
    current_program = None
    for line in file:
        # Detect the program being run
        for program in programs:
            if f"./{program}" in line:
                current_program = program
                break
        # Detect and capture the real time for each program and input size
        real_match = re.search(r"real\s+([\d.]+)", line)
        if real_match and current_program:
            real_time = float(real_match.group(1))
            real_times[current_program].append(real_time)

# Plotting the data
bar_width = 0.2
x = range(len(input_sizes))  # x positions for input sizes

# Create a bar for each program
plt.figure(figsize=(12, 6))
for i, program in enumerate(programs):
    # Offset each program's bars
    offset_x = [pos + (i - 1.5) * bar_width for pos in x]
    plt.bar(offset_x, real_times[program], width=bar_width, label=program)

# Add labels and title
plt.xlabel('Input Size')
plt.ylabel('Real Time (s)')
plt.title('Performance Comparison of Programs by Real Time')
plt.xticks(x, input_sizes)
plt.legend(title='Programs')
plt.tight_layout()

# Show the plot
plt.show()
