def convert(celsius):
    tempFahrenheit = celsius * 1.8 + 32
    return tempFahrenheit

def table():
    print('  F     C')
    for i in range(-30, 41, 10):
        fahrenheit = convert(i)
        print('{:5.1f} {:5.1f}'.format(fahrenheit, i))
table()


