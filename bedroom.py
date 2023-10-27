class Bed:
    '''
    models a bed
    it has a class variable _TYPE_SIZE (dict) {bed type:floor area}
    it has 3 attributes: type (str), price (float), description (str)
    it has property and getter method for price and floorArea
    it has __str__() method'''
    
    _TYPE_SIZE = {'Single': 1.73, 'Super': 2.03}
    
    def __init__(self, type, price, description):
        self._type = type
        self._price = price
        self._description = description
        
    @property
    def price(self):
        return self._price
    
    @property
    def floorArea(self):
        return self._TYPE_SIZE[self._type]
    
    def __str__(self):
        return f'{self._description}, ${self._price:.2f}'

class BookingException(Exception):
    '''subclass of Exception
    used when error encountered during booking'''
    
class MinFloorAreaException(Exception):
    '''subclass of Exception
    used when floor area rule is violated'''
    
class Room:
    '''models a room
    has 2 class variables: _MIN_EXIT_SPACE and _TYPE_SIZE
    has 4 attributes: _type (str), _roomPrice (float), _bed (Bed), _amenities (list)
    has property methods for _type, _roomPrice, and fullPrice
    has mutator methods: addAmenity() and removeAmenity()
    it has __str__() method'''
    
    _MIN_EXIT_SPACE = 1.84
    
    _TYPE_SIZE = {'Standard': 4.2, 'Deluxe': 4.83}
    
    def __init__(self, type, roomPrice, bed):
        self._type = type
        self._roomPrice = roomPrice
        self._bed = bed
        self._amenities = []
        
    @property
    def type(self):
        return self._type
    
    @property
    def roomPrice(self):
        return self._roomPrice
    
    @property
    def fullPrice(self):
        amenity_price = 0
        for n in self._amenities:
            amenity_price += n.price
        total = self._roomPrice + self._bed.price + amenity_price
        return total
    
    def addAmenity(self, newItem):
        amenity_floorArea = 0
        for n in self._amenities:
            amenity_floorArea += n.getFloorArea()
        self._floorarea = Room._TYPE_SIZE[self._type] - self._bed.floorArea - amenity_floorArea
        try:
            if newItem in self._amenities:
                raise BookingException (f'Error! This amenity ({newItem._description}) has already been added to this room.')
            if (self._floorarea - newItem.getFloorArea()) < Room._MIN_EXIT_SPACE:
                raise MinFloorAreaException (f'Error! Minimum available floor area must be at least {Room._MIN_EXIT_SPACE} sqm.')
        except Exception as e:
            print (e)
        else:
            self._amenities.append(newItem)
            return True
            
    def __str__(self):
        txt = ''
        for n in self._amenities:
            txt += f'{n._description}, ${n.price:.2f}\n'
        return f'{self._type} room, ${self._roomPrice:.2f}\n{self._bed}\n{txt}Full Price: ${self.fullPrice:.2f}'
    
    def removeAmenity(self, code):
        index = -1
        for i, j in enumerate (self._amenities):
            if j.itemCode == code:
                index = i
        if index == -1:
            raise BookingException (f'Error! No such amenity ({code}) in this room.')
        else:
            self._amenities.pop(index)