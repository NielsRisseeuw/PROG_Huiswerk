def standaardprijs(afstandKM):

    if afstandKM > 50:
        standaardprijs = 15 + (0.60 * afstandKM)

        return standaardprijs

    else:
        standaardprijs = 0.80 * afstandKM

        return standaardprijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs = standaardprijs(afstandKM)
    if leeftijd < 12 or leeftijd > 65:
        if weekendrit == 'ja':
            eindprijs = prijs * 0.66
        else:
            eindprijs = prijs * 0.7
    else:
        if weekendrit == 'ja':
            eindprijs = prijs * 0.6
        else:
            eindprijs = prijs
    return eindprijs

afstandKM = eval(input('Wat is de afstand in KM: '))
weekendrit = input('Is uw reis in het weekend: ')
leeftijd = eval(input('Wat is uw leeftijd: '))
prijs = ritprijs(leeftijd, weekendrit, afstandKM)
print('Uw reis kost: ' + str(prijs))
