# Functie
def eindbedrag(bedrag, rente):
    eindbedrag = bedrag + (rente * bedrag/100)
    print('Uw opgebouwde rente is: {}'.format(eindbedrag))
# Invoer creëren
rente = eval(input('Geef een rentepercentage: '))
bedrag = eval(input('Geef een startbedrag: '))
print('Dit programma berekend nu uw rente!')
print('.')
print('.')
print('.')
print('.')
print('.')
print('Ding!')
# Aanroepen funcie dmv. funtie met parameters
eindbedrag(bedrag, rente)
