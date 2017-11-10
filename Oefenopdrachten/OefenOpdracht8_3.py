def code(invoerstring):
    nieuwestring = ''
    for kar in invoerstring:
        nieuweASCII = ord(kar) + 3
        nieuwekar = chr(nieuweASCII)
        nieuwestring += nieuwekar
    return nieuwestring

invoerstring = str
naam = input('Voer uw naam in: ')
beginstation = input('Voer uw beginstation in: ')
eindstation = input('Voer uw eindstation in: ')
uitvoerstring = naam + beginstation + eindstation
print(uitvoerstring)
print(code(uitvoerstring))