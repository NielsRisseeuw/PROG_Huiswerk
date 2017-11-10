def ticker():
    infile = open('ticker.txt', 'r')
    regels = infile.readlines()
    infile.close
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].strip()
        tickerdict[sleutel] = waarde
    return tickerdict

tickerbestand = ticker()
bedrijfsnaam = input('Geef bedrijfsnaam: ')

for naam in tickerbestand:
    if naam == bedrijfsnaam:
        print(tickerbestand[naam])

code = input('Geef code: ')
for naam in tickerbestand:
    if code == tickerbestand[naam]:
        print(naam)


