invoer = input('Voer iets in: ')
if invoer == 'iets'  or invoer == 'Iets':
    print('Grapjas')
else:
    for karakter in invoer:
        asc = ord(karakter)
        print('{} {} {:b} {:x}'.format(karakter, asc, asc, asc))
