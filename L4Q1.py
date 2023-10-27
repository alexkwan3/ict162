class BoxException(Exception):
    '''subclass of Exception
    use when error encountered using Box object'''
    
class Box:
    '''models a box
    it has a class attribute: _max representing max items allowed
    it has one instance attribute: numItems(int)
    it has mutator methods: remove() and add()
    it has __str__()'''
    
    '''may raise BoxException when number of items is greater than maximum allowed'''
    
    _maxItems = 10
    
    def __init__(self, numItems):
        if numItems > Box._maxItems:
            raise BoxException (f'Error! Cannot create box because it exceeds maximum allowed: {Box._maxItems}')
        else:
            self._numItems = numItems

    def __str__(self):
        return f'Number of items: {self._numItems}'
    
    '''may raise BoxException when number of items to be added exceed maximum allowed'''
    
    def add(self, items):
        if self._numItems + items <= self._maxItems:
            self._numItems += items
            return self._numItems
        else:
            raise BoxException (f'Error! Cannot add items to box because it exceeds the maximum allowed: {Box._maxItems}')
    
    def remove(self, items):
        if self._numItems - items < 0:
            raise BoxException (f'Error! Cannot remove items from box as {items} exceeds the number of items in the box: {self._numItems}.')
        else:
            self._numItems -= items
            return self._numItems
    
def test():
    try:
        box = Box(5)
        print (box)
        box.add(5)
        print (box)
        box.remove(4)
        print (box)
    except BoxException as e:
        print (e)    
test()