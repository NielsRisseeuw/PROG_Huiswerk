invoer = '5-9-7-1-7-8-3-2-4-8-7-9'

invoer = invoer.split('-')

invoer = [int(i) for i in invoer]

invoer.sort()

maxGetal = max(invoer)
minGetal = min(invoer)
lengte = len(invoer)
SomInvoer = sum(invoer)
gemiddelde = (sum(invoer)/len(invoer))

print('Gesorteerde list van ints: {}'.format(invoer))
print('Grootste getal: {} en Kleinste getal: {}'.format(maxGetal, minGetal))
print('Aantal getallen: {} en Som van de getallen: {}'.format(lengte, SomInvoer))
print('Gemiddelde: {}'.format(gemiddelde))