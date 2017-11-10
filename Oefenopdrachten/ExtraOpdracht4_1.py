temperatuur = eval(input('Wat is de temperatuur vandaag: '))

if temperatuur <= 0:
    print('Het vriest vandaag')
elif temperatuur > 0 and temperatuur <= 15:
    print('Het is koud vaandaag')
else:
    print('Het is lekker warm vandaag')