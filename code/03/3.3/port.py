# port.py

import csv

total = 0.0

with open('../../Data/portfolio2.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)   # Skip the header row
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2] * row[3]

print('Total cost:', total)


# working on a higher level 
# csv library is doing a lot of data preparation out-of-the-box
total = 0.0
with open('../../Data/portfolio.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)   # Skip the header row
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2] * row[3]

print('Total cost:', total)