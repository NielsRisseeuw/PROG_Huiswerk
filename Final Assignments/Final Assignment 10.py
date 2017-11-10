import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary


stationsdict = processXML('FA10.xml')
stations = stationsdict['Stations']['Station']

print('Dit zijn de codes en type van de 4 stations: ')
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print('\nDit zijn alle stations met één of meer synoniemen: ')
for station in stations:
    if station['Synoniemen'] is not None:
        print('{:4} - {}'.format(station['Code'], station['Synoniemen']))

print('\nDit is de lange naam vam elk station: ')
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))