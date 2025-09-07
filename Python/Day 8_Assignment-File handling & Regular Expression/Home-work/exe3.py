# reading csv file
import csv
with open ('text2.csv', 'r')as file:
    reader=csv.reader(file)
    print(reader)

print("============================================>")
print("Printing data in rows format")
# reading data in rows format
with open ('text2.csv', 'r')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)

print("============================================>")
print("Printing data in columns format")
# reading csv file in dcolumns format
with open ('text2.csv', 'r')as file:
    reader=csv.reader(file)
    for column in zip(*reader):
        print(column)

print("============================================>")
print("Printing data in list format")
# reading csv file in list format
with open ('text2.csv', 'r')as file:
    reader=csv.reader(file)
    data=list(reader)
    print(data)
    
print("============================================>")
print("Printing data in dictionary format")
# reading csv file in dictionary format
with open ('text2.csv', 'r')as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)
        
