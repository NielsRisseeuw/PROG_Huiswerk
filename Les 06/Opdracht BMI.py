gewicht = eval(input('Wat is uw gewicht: '))
lengte = eval(input('Wat is uw lengte in centimeters: '))

bodymassindex = 0

bodymassindex = gewicht / (lengte**2)

if bodymassindex <= 18.5:
    print('Ondergewicht')

elif bodymassindex > 18.5 and bodymassindex < 25:
    print('Normaal')

else:
    print('Overgewicht')

print('Uw BMI is {} x {}: {}' .format(gewicht, lengte, bodymassindex))

