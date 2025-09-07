# Read CSV file Having Tab Delimiter -- \t
import csv
with open ('text2.csv', 'r', newline='') as file:
    reader=csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
