zin = input('Typ een zin: ')

woorden = zin.split()

acroniem = ''

for woord in woorden:
    acroniem = acroniem + woord[0].upper()

print(acroniem)