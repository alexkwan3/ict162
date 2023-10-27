from datetime import datetime

class Flight:
    def __init__(self, flightNo, destination, departureDate): 
        self._flightNo = flightNo
        self._destination =destination
        self._departureDate = departureDate
        
    @property
    def flightNo(self): return self._flightNo
    @property
    def destination(self): return self._destination
    @property
    def departureDate (self): return self._departureDate
    
    @flightNo.setter
    def flightNo(self, flightNo): self._flightNo = flightNo
    
    @departureDate.setter
    def departureDate (self, departureDate): self._departureDate = departureDate
    
    def __str__(self):
        return f'Flight: {self._flightNo} Destination: {self._destination} Departure ' +\
            f'Date: {self._departureDate:%d/%m/%Y %H:%M }'
            
class Passenger:
    '''models a passenger
    it has 3 attributes: ppNo (str), name (str), and flight (Flight)
    it has property method for ppNo, name, and flight
    it has setter method for flight
    it has getDepartureDate() method
    it has __str__() method'''
    
    def __init__(self, ppNo, name, flight):
        self._ppNo = ppNo
        self._name = name
        self._flight = flight
        
    @property
    def ppNo(self): return self._ppNo
    @property
    def name(self): return self._name
    @property
    def flight(self): return self._flight
    
    @flight.setter
    def flight(self, newFlight): self._flight = newFlight
    
    def getDepartureDate(self): return self._flight.departureDate
    
    def __str__(self):
        return f'Name: {self._name} {self._flight}'
    
class Booking:
    '''models a booking
    it has a class attribute: bkNum
    it has 3 object's attributes: bookingID, passenger, and flight
    it has property methods for bookingID, passenger, and flight
    it has __str__() method
    '''
    
    _bkNum = 1 # class variable
    
    def __init__ (self,pax,flight):
        self._pax = pax
        self._flight = flight
        self._bookingID = Booking._bkNum
        Booking._bkNum += 1 # update class variable
    
    @property
    def bookingID(self): return self._bookingID
    @property
    def pax(self): return self._pax
    @property
    def flight(self): return self._flight
    
    @flight.setter
    def flight(self,newFlight): self._flight = newFlight
    
    def __str__(self):
        return f'Booking ID: {self._bookingID}\n{self._pax}\n{self._flight}'
    
class Airline:
    '''models an airline
    it has 2 attributes: name (str) and bookings (dict)
    it has accessor method: searchBookings()
    it has addBooking(), deleteBooking(), and changeBooking() methods
    it has __str__() method'''
    
    def __init__(self, name):
        self._name = name
        self._bookings = {} # initially empty dictionary; key is bookingID; value is booking object
        
    def addBooking(self, booking):
        '''accepts a booking object, booking, and attempts to add to the collection
        return True if successful; otherwise return False'''
        if booking.bookingID not in self._bookings.keys():
            self._bookings[booking.bookingID] = booking
            return True
        else:
            return False
        
    def searchBooking(self, bkID):
        '''accepts an ID, bkID, and searches for the corresponding booking that has
        this ID; return the booking object if found; otherwise return None'''
        if bkID in self._bookings.keys():
            return self._bookings[bkID]
        else:
            return None
    
    def deleteBooking(self, bkID):
        '''accepts an ID, bkID, and attempt to remove the Booking object with the bkID;
        return True if can remove; otherwise return False'''
        bk = self.searchBooking(bkID)
        if bk is None:
            return False
        else:
            self._bookings.pop(bkID) # removes the entire entry from the dict
            return True
        
    def changeBooking(self, bkID, newFlight):
        '''accepts an ID, bkID, and a flight object, newFlight
        if booking with the given ID is found, update the flight object of the booking, return True;
        otherwise return False'''
        bk = self.searchBooking(bkID)
        if bk is None:
            return False
        else:
            bk.flight = newFlight
            return True
    
    def __str__(self):
        '''returns a string containing all bookings'''
        txt = ''
        for v in self._bookings.values():
            txt += f'{v}\n'
        return txt
        
    
def main():
    d = datetime (2023, 4, 5, 23, 45)
    f = Flight('SQ001', 'LA', d)
    # print (f)
    pa = Passenger ('1234', 'Tan KK', f)
    # print (pa)
    d2 = datetime(2023, 4, 23, 8, 15)
    f2 = Flight ('SQ123', 'LON', d2)
    pa.flight = f2 # calls the setter method
    # print (pa)
    # print departure date of pa
    # print (pa.getDepartureDate())
    # print (f'{pa.getDepartureDate():%d-%m-%Y %H:%M}')
    # print (f'{pa.getDepartureDate():%d %b %Y %H:%M}')
    bk = Booking(pa,f)
    # print (bk)
    pa2 = Passenger('7787', 'John', f2)
    bk2 = Booking(pa2, f)
    print (bk2)
    ar = Airline('VietJet')
    ar.addBooking(bk)
    ar.addBooking(bk2)
    print (ar)
    b = ar.searchBooking(2)
    if b is None:
        print ('Not found')
    else:
        print (f'Found - {b}')
    ar.changeBooking(1, f2)
    print (f'After change: {ar}')
    if ar.deleteBooking(2):
        print ('Booking removed')
        print (f'After removing: {ar}')
    else:
        print ('Cannot remove')
main()