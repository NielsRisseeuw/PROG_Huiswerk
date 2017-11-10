getallenrij = [23, 35, 31, 26, 73, 75, 84, 29, 42, 46]

def berekensomevengetallen(getallenrij):
    som = 0
    for getal in getallenrij:
        if getal % 2 == 0:
            som += getal
    return som

def berekenSomOneverGetallen(getallenrij):
    OnevenSom = 0
    for getal in getallenrij:
        if getal % 2 == 1:
            OnevenSom += getal
    return OnevenSom

OnevenSom = berekenSomOneverGetallen(getallenrij)
som = berekensomevengetallen(getallenrij)
print('De som van de even getallen bedraagt: {}'.format(som))
print('De som van de oneven getallen bedraagt: {}'.format(OnevenSom))