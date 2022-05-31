# Generator Usage
import csv
# CSV Reader

file = open("salary_data.csv")
csv_reader = csv.reader(file)
print('Header:', next(csv_reader))
for row in csv_reader:
    print(row)