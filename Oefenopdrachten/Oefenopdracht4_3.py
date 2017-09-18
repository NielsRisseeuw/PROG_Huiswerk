def lang_genoeg(lengte):
    if lengte >= 120:
        return True

    else:
        return False
lengte = eval(input('Wat is uw lengte: '))
if lang_genoeg(lengte):
    print('Je bent lang genoeg voor de attractie!')

else:
    print('Je bent te klein voor de attractie ¯\_(ツ)_/¯ ')