from amenity import *
    
def q2():
    SA1 = SharedAmenity('Wi-Fi', 'One-day Wi-Fi pass', 1)
    SA2 = SharedAmenity('Breakfast', 'Breakfast buffet at Sun café (#01-01 6AM to 10AM)', 8.99)
    IRA1 = InRoomAmenity('IRON-B', 'Iron and ironing board (128cm x 30cm)', 2.99, 0.4)
    IRA2 = InRoomAmenity('DESK-W', 'Writing desk (80cm x 55cm)', 3.99, 0.44)
    amenities = [SA1, SA2, IRA1, IRA2]
    total_price = 0
    total_area = 0
    for n in amenities:
        total_price += n.price
        total_area += n.getFloorArea()
    print (f'Total: {total_area:.2f} square metres, ${total_price:.2f}')
q2()