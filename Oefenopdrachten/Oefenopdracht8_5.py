import random
def diceprob(invoersom):
    aantalworpen=0
    aantalworpinv=0
    while aantalworpinv<100:
        dobbelsteen1=random.randrange(1,7)
        dobbelsteen2=random.randrange(1,7)
        som=dobbelsteen1 + dobbelsteen2
        if som==invoersom:
            aantalworpinv+=1
        aantalworpen+=1
    print('Het aantal benodige worpen is {}'.format(aantalworpen))

somaantalogen = eval(input('Hoe groot is de som: '))
diceprob(somaantalogen)
