import csv
with open('stations.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter = ';')
    for row in reader:
        print(row[0], row[2])

with open('stations.csv', 'r') as myCSVFile:
    reader = csv.Dictreader(myCSVFile, delimiter = ';')
    for row in reader:
        print(row['name'], row['type'])
