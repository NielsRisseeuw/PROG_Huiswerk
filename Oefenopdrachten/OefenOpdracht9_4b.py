import csv

# Kolom koppen inlezen met DictReader!

with open('producten.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter = ';')
    maxprijs = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > maxprijs:
            maxprijs = prijs
            maxnaam = row['Naam']
print('Het duurste artikel is {} en die kost {} Euro'.format(maxnaam, maxprijs))