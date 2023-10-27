from guest import *
        
def q1():
    d = date (2023, 2, 12)
    guest = Guest('123445678', 'Kyrie Irving', 'USA')
    guest.blacklist(d, 'Drunk and disorderly')
    guest.blacklist(d, 'Assault employees')
    print (guest)
    print (guest.isBlacklisted())
q1()