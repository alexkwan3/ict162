from amenity import *
from bedroom import *
            
def q3():
    try:
        fridge = InRoomAmenity('FRIDGE', 'Mini Fridge (50L)', 4.59, 0.25)
        chair = InRoomAmenity('CHAIR', 'Foldable Chair (42cm x 38cm)', 2.59, 0.16)
        desk = InRoomAmenity('DESK-W', 'Writing desk (80cm x 55cm)', 3.99, 0.44)
        iron = InRoomAmenity('IRON-B', 'Iron and ironing board (128cm x 30cm)', 2.99, 0.4)
        gympass = SharedAmenity('GYM-PEP', 'Per entry pass to gym (Level 04-01)', 1.00)
        wifi = SharedAmenity('WI-FI', 'One-day Wi-Fi access', 1.00)
        bedtype1 = Bed('Single', 10.99, 'Single bed with one pillow and one blanket')
        bedtype2 = Bed('Super', 12.99, 'Super single bed with one pillow and one blanket')
        roomtype1 = Room('Standard', 16.99, bedtype1)
        roomtype2 = Room('Deluxe', 19.99, bedtype2)
        roomtype1.addAmenity(gympass)
        roomtype1.removeAmenity('GYM-PEP')
        roomtype1.addAmenity(fridge)
        roomtype1.removeAmenity('FRIDGE')
        roomtype1.addAmenity(wifi)
        roomtype1.addAmenity(gympass)
        roomtype2.addAmenity(fridge)
        roomtype2.removeAmenity('FRIDGE')
        roomtype2.addAmenity(chair)
        roomtype2.addAmenity(desk)
        roomtype2.addAmenity(iron)
    except Exception as be:
        print (be)
    finally:
        print (roomtype1)
        print ()
        print (roomtype2)
q3()