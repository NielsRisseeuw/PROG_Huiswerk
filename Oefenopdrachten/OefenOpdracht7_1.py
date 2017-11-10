counter = 0
uitvoer = 0
invoer = int

while invoer != 0:
    getal = eval(input('Geef een getal: '))
    counter += 1
    if getal != 0:
        uitvoer = (uitvoer+getal)
    else:

        print('Er zijn {} getallen ingevoerd, de som is: {}'.format((counter-1), uitvoer))
