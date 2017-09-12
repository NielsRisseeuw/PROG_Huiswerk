naam  = input('Wat is jou naam: ')
leeftijd = eval(input('Wat is je leeftijd: '))

if leeftijd < 18:
    print(naam + ', Je mag niet stemmen')

else:
    print(naam + ', Je mag wel stemmen')