tabel = [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]
aantal = 0
aantalrijen = len(tabel)
aantalkolommen = len(tabel[0])
for rij in range(aantalrijen):
    for kolom in range(aantalkolommen):
        if tabel[rij][kolom] > 0:
            aantal = aantal + 1

print(aantal)
