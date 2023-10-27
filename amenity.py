from abc import ABC, abstractmethod

class Amenity(ABC):
    '''this is an abstract class
    it has 3 attributes: _itemCode (str), _description (str), and _price (float)
    it has property and getter methods for itemCode and price
    it has an abstract method: getFloorArea()
    it has __str__() method'''
    
    def __init__(self, itemCode, description, price):
        self._itemCode = itemCode
        self._description = description
        self._price = price
        
    @property
    def itemCode(self):
        return self._itemCode
    
    @property
    def price(self):
        return self._price
    
    @itemCode.getter
    def itemCode(self):
        return self._itemCode
    
    @price.getter
    def price(self):
        return self._price
    
    def getFloorArea(self):
        pass
    
    def __str__(self):
        return f'{self._itemCode}, {self._description}, ${self._price:.2f}'
    
class SharedAmenity(Amenity):
    '''subclass of Amenity
    it overrides the getFloorArea() method'''
    
    def __init__(self, itemCode, description, price):
        super().__init__(itemCode, description, price)
        
    def getFloorArea(self):
        return 0
    
class InRoomAmenity(Amenity):
    '''subclass of Amenity
    it has 1 additional attribute: _floorArea (float)
    it overrides the getFloorArea() method'''
    
    def __init__(self, itemCode, description, price, floorArea):
        super().__init__(itemCode, description, price)
        self._floorArea = floorArea
    
    def getFloorArea(self):
        return self._floorArea