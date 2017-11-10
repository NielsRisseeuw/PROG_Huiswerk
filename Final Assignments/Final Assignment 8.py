stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
            'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch',
            'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def inlezen_beginstation():
    beginstation=""
    while beginstation not in stations:
        beginstation = input('Geef beginstation: ')
    return beginstation

beginstation=inlezen_beginstation()

def inlezen_eindstation(beginstation):
    eindstation = ""
    while eindstation not in stations:
        eindstation = input('Geef eindstation: ')
        while stations.index(eindstation)<stations.index(beginstation):
            eindstation=input('fout geef iets dergelijkst')
        return eindstation
eindstation=inlezen_eindstation(beginstation)

def omroepen_reis(stations,beginstation,eindstation):
    nummerB=stations.index(beginstation)+1
    nummerE=stations.index(eindstation)+1
    print('Het beginstation is {} Het eindstation is {}'.format(beginstation,eindstation))
    afstand=nummerE-nummerB
    prijs=5*afstand
    for index in range(nummerB,nummerE-1):
        print(stations[index])
    print(prijs)
omroepen_reis(stations,beginstation,eindstation)
