woord = ''
lengteWoord = 0

while lengteWoord != 4:
    woord = input('Geef een string van 4 letters: ')
    lengteWoord = len(woord)
    if lengteWoord == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(woord))
        break
    else:
        print('{} heeft {} letters'.format(woord, lengteWoord))