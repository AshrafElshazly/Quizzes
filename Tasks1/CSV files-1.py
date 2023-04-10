import csv

with open("Tasks1/dict.csv",'r') as file:
    reader = csv.DictReader(file)
    data= list(reader)
print(data)