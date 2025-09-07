# csv.DictWriter(file, fieldnames)
import csv
with open ('player.csv', 'w')as file:
    fieldnames = ['player_name', 'fide_rating']
    #Returns CSV writer object
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Virat Kholi', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Rohit Sharma', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Rahul', 'fide_rating': 2801})
