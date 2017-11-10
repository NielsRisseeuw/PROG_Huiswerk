def seizoen(maand):

    if maand >= 0 and maand <= 2:
        resultaat = 'winter'

    elif maand >= 3 and maand <= 5:
        resultaat = 'lente'

    elif maand >= 6 and maand <= 8:
        resultaat = 'zomer'

    elif maand >= 9 and maand <= 11:
        resultaat = 'herfst'

    return resultaat

maandinput = eval(input('Wat is het maandnummer: '))
print(seizoen(maandinput))