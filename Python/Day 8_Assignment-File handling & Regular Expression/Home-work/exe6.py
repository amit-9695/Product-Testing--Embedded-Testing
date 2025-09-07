#Writing CSV files Using csv.writer()
import csv
with open('text2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Writing header
    writer.writerow(['Name', 'Email', 'Phone'])
    # Writing data
    writer.writerow(['Amit Shukla', 'amit.shukla@example.com', '123-456-7890'])
    writer.writerow(['Atul Shukla', 'atul.shukla@example.com', '123-456-7891'])
    writer.writerow(['Anjali Shukla', 'anjali.shukla@example.com', '123-456-7892'])
    