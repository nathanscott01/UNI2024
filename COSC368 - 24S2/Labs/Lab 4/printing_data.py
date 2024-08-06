"""
Nathan Scott
COSC368 Lab 4
Printing Data
"""

import pandas as pd
import csv
import math

data_file = pd.read_csv('mean_time_by_id.csv')

for i, row in data_file.iterrows():
    print(row["Mean Time"])
