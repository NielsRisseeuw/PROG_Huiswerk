infile = open('Voorbeeld5_5.txt', 'r')

inhoud1 = infile.read()

infile.close()
                    # Van de string een lijst maken gesplitst op de spatie toekennen aan een nieuwe variabele

inhoud2 = inhoud1.split()

print(inhoud2)