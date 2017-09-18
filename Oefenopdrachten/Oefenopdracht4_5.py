def kwadraten_som(grnd):
    x=0
    for v in grondgetallen:
        if v>0:
            x=x+(v**2)
    return x

grondgetallen=[4,5,3,-81]
getal=kwadraten_som(grondgetallen)
print (getal)
