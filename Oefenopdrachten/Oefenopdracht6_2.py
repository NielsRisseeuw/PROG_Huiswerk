lst = ['boter', 'kaas', 'bier', 'pizza', 'thee', 'thee', 'drop', 'koek', 'cola', 'boterham', 'stampot']
lst2 = []
for woord in lst:
    if len(woord) == 4:
        lst2.append(woord)
print('De nieuw gemaakte lijst met alle vier-letter strings is:\n{}'.format(lst2))