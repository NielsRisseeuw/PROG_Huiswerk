nummer = 0
factor = 0
uitkomst = 0

for i in range(0, 10):
    nummer += 1
    for c in range(0, 10):
        factor += 1
        if factor == 11:
            factor = 1
        uitkomst = nummer * factor
        if factor == 1:
            print(' ')
        print('{} x {} = {}'.format(nummer, factor, uitkomst))

