import csv

class CSVUtil:
    def read_data(file_path):
        data=[]
        with open(file_path,"r") as file:
            reader=csv.DictReader(file)
            for row in reader:
                data.append((row["username"],row["password"]))
        return data
        