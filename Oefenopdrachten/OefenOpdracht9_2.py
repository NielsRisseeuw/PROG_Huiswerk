import csv

with open('inloggers.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('naam', 'voorletter', 'geboortedatum', 'email', 'number'))

    while True:
        naam = input('Wat is je naam: ')
        if naam == 'einde' or naam == 'Einde':
            break

        voorletter = input('Wat is je voorletter: ')
        geboortedatum = input('Wat is je geboortedatum ') # Zonder datum wegschrijven? Is dat geboortedatum niet er bij,
        #  in dit gevall kan je get gewoon weghalen met een hashtag en de writerow aanpassen

        email = input('Wat is je email: ')
        number = input('Wat is je nummer: ')

        writer.writerow((naam, voorletter, geboortedatum, email, number))