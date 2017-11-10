import csv

with open('producten.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'))

    while True:
        artikelnummer = input('Geef een artikelnummer: ')
        if artikelnummer == 'einde' or artikelnummer == 'Einde':
            break
        artikelcode = input('Geef een artikelcode: ')
        naam = input('Geef een artikelnaam: ')
        voorraad = input('geef een vooraadnummer: ')
        prijs = input('Geef een prijs: ')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))