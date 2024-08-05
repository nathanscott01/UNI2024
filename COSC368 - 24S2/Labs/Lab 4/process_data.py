"""
Nathan Scott
COSC368 Lab 4
Process Fitts Test Data
"""

import pandas as pd
import csv
import math

columns = ["Distance", "Width", "Block Count", "Time Taken"]
data_file = pd.read_csv('fitts_tests.csv', usecols=columns)

# Filter the data to include only block numbers 3 to 8
filtered_data = data_file[(data_file["Block Count"] >= 3) & (data_file["Block Count"] <= 8)]

averaged_data = filtered_data.groupby(["Distance", "Width"]).agg({"Time Taken" : "mean"}).reset_index()

time_dict = {}

for i, row in data_file.iterrows():
    key = (row["Distance"], row["Width"])
    value = row["Time Taken"]
    time_dict[key] = value
    
# Write the average time dictionary to a CSV file
with open('summary.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["Amplitude", "Width", "ID", "Mean Time"])
    
    # Write the data
    for (distance, width), avg_time in time_dict.items():
        index_difficulty = math.log2(distance / width + 1)
        index_difficulty = f"{index_difficulty:.3f}"
        writer.writerow([distance, width, index_difficulty, avg_time])
 

# Read the summary.csv to find mean time across the ID values
summary_data = pd.read_csv('summary.csv')        
        
# Group by ID and calculate the mean time
id_grouped_data = summary_data.groupby("ID").agg({"Mean Time": "mean"}).reset_index()

# Write the result to a new CSV file
with open('mean_time_by_id.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Write the header
    writer.writerow(["ID", "Mean Time"])
    
    # Write the data
    for i, row in id_grouped_data.iterrows():
        id_value = row["ID"]
        mean_time = row["Mean Time"]
        mean_time = f"{mean_time:.3f}"
        writer.writerow([id_value, mean_time])