from guest import *
from bedroom import *
from datetime import *
from amenity import *

class Booking:
    '''models a booking system
    it has a class variable: _NEXT_ID
    it has 7 attributes: _bookingID(str), _guest(Guest), _room(Room), _checkInDate(date), _checkOutDate(date), _allocatedRoomNo(str), _status(str)
    it has property methods for _bookingID, _checkInDate, _checkOutDate, _status, passport, roomType, totalPrice
    it has setter method for _status
    it has mutator method: checkIn()
    it has __str__() method'''
    
    _NEXT_ID = 1
    
    def __init__(self, guest, room, checkInDate, checkOutDate):
        self._guest = guest
        self._room = room
        self._CID = checkInDate
        self._COD = checkOutDate
        self._bookingID = Booking._NEXT_ID
        Booking._NEXT_ID += 1 # updates the class variable
        self._allocatedRoomNo = None
        self._status = 'Pending'
        if self._guest.isBlacklisted() == True:
            raise BookingException (f'Guest {self._guest.name} is blacklisted.')
        if self._COD <= self._CID:
            raise BookingException (f'Check out date must be at least 1 day after check in date.')
         
    @property
    def bookingID(self):
        return self._bookingID
    
    @property
    def checkInDate(self):
        return self._CID
    
    @property
    def checkOutDate(self):
        return self._COD
    
    @property
    def status(self):
        return self._status
    
    @property
    def passport(self):
        return self._guest.passport
    
    @property
    def roomType(self):
        return self._room.type
    
    @property
    def totalPrice(self):
        nights = self._COD - self._CID
        total = self._room.fullPrice * nights.days
        return total
    
    @status.setter
    def status(self, newStatus):
        self._status = newStatus
        
    def checkIn(self, roomNum):
        if self._status != 'Confirmed':
            raise BookingException ("Error! Booking not confirmed.")
        elif self._CID != datetime.today().date(): 
            # if check in must be done on check in date, check in date would be today
            raise BookingException ("Error! Today is not the check in date.")
        else:
            self._status = 'Checked-in'
            self._allocatedRoomNo = roomNum
    
    def __str__(self):
        nights = self._COD - self._CID
        txt = f'\nBooking ID: {self._bookingID}\n' +\
        f'Passport Number: {self.passport}\n' +\
        f'Name: {self._guest.name}\n' +\
        f'Check-in/out dates: {self._CID:%d-%b-%Y} / {self._COD:%d-%b-%Y}\n' +\
        f'Booking Status: {self._status}\n' +\
        f'\n{self._room.__str__()}\n' +\
        f'\nTotal price: ${self._room.fullPrice:.2f} x {nights.days} nights = ${self.totalPrice:.2f}'
        return txt