from abc import ABC, abstractmethod

from datetime import datetime, date

class Flight:
    def __init__(self, flightNo, destination, departureDate, fare): 
        self._flightNo = flightNo
        self._destination = destination
        self._departureDate = departureDate
        self._fare = fare
        
    @property
    def flightNo(self): return self._flightNo
    @property
    def destination(self): return self._destination
    @property
    def departureDate (self): return self._departureDate
    @property
    def fare(self): return self._fare
    
    @flightNo.setter
    def flightNo(self, flightNo): self._flightNo = flightNo
    
    @departureDate.setter
    def departureDate (self, departureDate): self._departureDate = departureDate
    
    def __str__(self):
        return f'Flight: {self._flightNo} Destination: {self._destination} Departure ' +\
            f'Date: {self._departureDate:%d/%m/%Y %H:%M} Fare: ${self._fare:.2f}'
            
class Passenger:
    '''models a passenger
    it has 3 attributes: ppNo (str), name (str), and yearBorn (int)
    it has property method for ppNo, name, and yearBorn
    it has __str__() method'''
    
    def __init__(self, ppNo, name, yearBorn):
        self._ppNo = ppNo
        self._name = name
        self._yearBorn = yearBorn
        
    @property
    def ppNo(self): return self._ppNo
    @property
    def name(self): return self._name
    @property
    def yearBorn(self): return self._yearBorn
    
    def __str__(self):
        return f'Name: {self._name} {self._yearBorn}'
    
class Booking(ABC):
    '''models a booking
    it has a class attribute: bkNum
    it has 3 object's attributes: bookingID, passenger, flight, and bkDate
    it has property methods for bookingID, passenger, flight, and bkDate
    it has an abstract method: ticketPrice()
    it has __str__() method'''
    
    _bkNum = 1 # class variable
    
    def __init__ (self, pax, flight, bkDate):
        self._pax = pax
        self._flight = flight
        self._bookingID = Booking._bkNum
        Booking._bkNum += 1 # update class variable
        self._bkDate = bkDate
    
    @property
    def bookingID(self): return self._bookingID
    @property
    def pax(self): return self._pax
    @property
    def flight(self): return self._flight
    @property
    def bkDate(self): return self._bkDate
    
    @flight.setter
    def flight(self,newFlight): self._flight = newFlight
    
    @abstractmethod
    def ticketPrice(self):
        pass
    
    def __str__(self):
        return f'Booking ID: {self._bookingID}\n{self._pax}\n{self._flight}\nBooking Date: {self._bkDate: %d/%m/%Y %H:%M} Ticket price: ${self.ticketPrice():.2f}'
            
class IndividualBooking(Booking):
    '''subclass of Booking
    it has a class variable: discount
    it has no additional attributes
    it overrides ticketPrice()'''
    
    _discount = 0.2
    
    def __init__ (self, pax, flight, bkDate):
        super().__init__(pax, flight, bkDate)
        
    def ticketPrice(self):
        age = date.today().year - self._pax.yearBorn
        price = self._flight.fare
        if age < 18 or age >= 60:
            price = price * (1 - IndividualBooking._discount)
        return price

class CorporateBooking(Booking):
    '''subclass of Booking
    it has class variable: discount
    it has an additional attribute: coyName (str)
    it overrides ticketPrice()'''
    
    _discount = 0.5
    
    def __init__(self, pax, flight, bkDate, coyName):
        super().__init__(pax, flight, bkDate)
        self._coyName = coyName
    
    def ticketPrice(self):
        price = self._flight.fare * self._discount
        return price
    
    def __str__(self):
        return f'{super().__str__()}\nCompany: {self._coyName}'
    
class BookingException(Exception):
    '''to handle errors relating to booking'''
    
class Airline:
    ''' it has 2 attributes: name (str) and bookings (dict)
    it has mutator methods: add, search, delete, change
    it has __str__()'''
    
    def __init__(self, name):
        self._name = name
        self._bookings = {} # key is booking id and value is booking object
        
    '''may raise BookingException when ID exists or when booking date is after flight departure date'''
    
    def addBooking(self, bk):
        if bk.bookingID in self._bookings.keys():
            raise BookingException ("Cannot add booking, already exists!")
        elif bk.bkDate > bk.flight.departureDate:
            raise BookingException ("Cannot add, booking date is after departure date!")
        else:
            self._bookings[bk.bookingID] = bk
            
    def __str__(self):
        '''returns a single string that contains all booking objects details'''
        txt = 'Bookings\n'
        for bk in self._bookings.values():
            txt += f'{bk}\n'
        return txt
    
    def searchBooking(self,bkID):
        if bkID in self._bookings.keys():
            return self._bookings[bkID]
        else:
            return None
        
    def deleteBooking(self, bkID):
        bk = self.searchBooking(bkID)
        if bk is None:
            raise BookingException ("Cannot delete, booking ID not found.")
        elif bk.flight.departureDate < datetime.today():
            raise BookingException ("Cannot delete, flight has departed.")
        else:
            self._bookings.pop(bkID)
    
    def changeBooking(self, bkID, newFlight):
        bk = self.searchBooking(bkID)
        if bk is None:
            raise BookingException ('Cannot change, booking ID not found.')
        elif newFlight.departureDate < bk.bkDate:
            raise BookingException ("Cannot change, departure date is earlier than booking date.")
        else:
            bk.flight = newFlight
    
def q3():
    d = datetime (2023, 4, 5, 23, 45)
    f = Flight('SQ001', 'LA', d, 1300)
    pa1 = Passenger('b123', 'Tom', 1976)
    pa2 = Passenger('b876', 'Kim Teck', 1955)
    # print (pa1)
    # print (pa2)
    # print (f)
    d2 = datetime(2023, 4, 1, 14, 15)
    inBk1 = IndividualBooking(pa1, f, d2)
    print (inBk1)
    inBk2 = IndividualBooking(pa2, f, d2)
    print (inBk2)
    corpBk1 = CorporateBooking(pa1, f, d2, 'SingTel')
    print (corpBk1)
    corpBk2 = CorporateBooking(pa2, f, d2, 'SUSS')
    print (corpBk2)
    
    coy = Airline('MyAir')
    d3 = datetime(2023, 5, 6, 11, 35)
    f2 = Flight('SQ999', 'NY', d3, 1500)
    try:
        coy.addBooking(inBk1)
        # coy.addBooking(inBk1)
        b = coy.searchBooking(2)
        if b is not None:
            print (f'Found booking: {b}')
        else:
            print ("Booking not found.")
        coy.changeBooking(1, f2)
        # coy.deleteBooking(1)
    except BookingException as e:
        print (e)
    
    print ('****** test airline ******')
    print (coy)
q3()