# python script to read a CSV file with tab delimiter and print each row
import csv
with open('text2.csv', 'r')as file:
     reader = csv.DictReader(file, delimiter = '\t')
     print(reader)
     for row in reader:
         print(row)
