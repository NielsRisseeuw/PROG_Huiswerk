cijferICOR = float(input('Wat is je cijfer voor ICOR: '))
cijferPROG = float(input('Wat is je cijfer voor PROG: '))
cijferCSN = float(input('Wat is je cijfer voor CNS: '))

cijferGem = (cijferICOR + cijferCSN + cijferPROG)/3

print ('Mijn cijfers (gemiddeld een ' + str(round(cijferGem,1)) + ') leveren een beloning van € ' + str(cijferGem*90) + ' euro op!')

