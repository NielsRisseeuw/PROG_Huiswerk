def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >=6:
        for c in newpassword:
            if c in '0123456789':
                return True
        else:
            return False
    else:
        return False
# Correcte wachtwoordden --> True
res = new_password('vakProg', 'python17')
print (res)

# Hetzelfde wachtwoord --> False
print(new_password('huProg17', 'huProg17'))

# Te kort nieuw wachtwoord --> False
print(new_password('vakProg17', 'Pro17'))

# Geen cijfer in wachtwoord --> True
print(new_password('vakprog', 'vakprogrammeur17'))