def toon_aantal_kluizen_vrij():
    infile = open('kluizen.txt','r')
    inhoud = infile.readlines()
    aantal = len(inhoud)
    infile.close()
    return aantal
def nieuwe_kluis():
    lst = [1,2,3,4,5,6,7,8,9,10,11,12]
    infile = open('kluizen.txt','r')
    regels = infile.readlines()
    infile.close()
    for kluis in regels:
        datavankluis = kluis.split(';')
        for nmr in lst:
            if datavankluis[1] == nmr:
                lst = lst.remove(nmr)
    print(lst)
    return


def nieuwe_kluis():
    kluisnummers = []
    for i in range(1, 13):
        kluisnummers.append(i)

    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()

    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringnummer = gegevensvan1kluis[0]
        nummer = int(stringnummer)
        kluisnummers.remove(nummer)

    if len(kluisnummers) > 0:
        nieuwkluisnummer = kluisnummers[0];
        print('Je kluisnummer is {}'.format(nieuwkluisnummer))
        code = input('Voer een code in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('{};{}\n'.format(nieuwkluisnummer, code))
        outfile.close()
    else:
        print('Er is geen kluis meer beschikbaar')

def kluis_openen():
    infile = open ('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('wat is je kluis: ')
    code = input ('Wat is je code: ')
    gegevenscorrect = False
    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringkluisnummer =gegevensvan1kluis[0]
        kluiscode = gegevensvan1kluis[1].strip()
        if stringnummer == stringkluisnummer and kluiscode == code:
            gegevenscorrect = True
    if gegevenscorrect == True:
        print ('Kluis {} word geopend.'.format(stringnummer))
    else:
        print ('Dit is niet de goede code.')
    return

def kluis_teruggeven():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is het nummer van je kluis: ')
    code = input('Wat is de code van je kluis: ')
    nieuwekluizendata = []
    for kluis in kluizendata:
        datavan1kluis = kluis.split(';')
        stringkluisnummer = datavan1kluis[0]
        kluiscode = datavan1kluis[1].strip()
        gegevenscorrect = (stringkluisnummer == stringnummer) and (kluiscode == code)
        if not gegevenscorrect:
            nieuwekluizendata.append(stringkluisnummer + ';' + kluiscode)
    outfile = open('kluizen.txt', 'w')
    for i in range(0, len(nieuwekluizendata)):
        outfile.write(nieuwekluizendata[i] + '\n')
    outfile.close()
    return

print('1: Ik wil weten hoeveel kluizen er nog beschikbaar zijn')
print('2: Ik wil een nieuwe kluis')
print('3: Ik wil even iets uit mijn kluis halen')
print('4: Ik geeft mijn kluis terug')
antw=eval(input('optie:'))
if antw==1:
    aantal=toon_aantal_kluizen_vrij()
    print('Er zijn {} kluizen vrij'.format(12-aantal))
if antw==2:
    nieuwe_kluis()
if antw==3:
    kluis_openen()
if antw==4:
    kluis_teruggeven()
if antw==str:
    print('Uw invoer is ongeldig')