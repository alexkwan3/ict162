class BankAccount:
    
    _interestRate = 0.03 # class variable
    
    def __init__(self, id, amount = 20): # optional or default value
        self._accountId = id 
        self._balance = amount
    
    @property
    def accountId(self):
        return self._accountId
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, amt):
        self._balance = amt
        
    def deposit(self, amount): 
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            return True
        return False

    def transfer(self, ba, amount): 
        if self.withdraw(amount):
            ba.deposit(amount)
            return True
        return False
    
    def accumulateInterest(self):
        self._balance += self._balance * type(self)._interestRate
        
    def __str__(self):
        return f'{self._accountId} {self._balance:.2f}'
    
class JuniorAccount(BankAccount):
    '''a subclass of BankAccount
    it has additional attribute: guardian (str)
    it has property method for guardian
    it overrides withdraw(), accumulateInterest(), and __str__()'''
    
    def __init__(self, id, guardian, amt):
        super().__init__(id, amt)
        self._guardian = guardian
        
    @property
    def guardian (self):
        return self._guardian
    
    # def withdraw(self, amt): # overriding by refinement
    #     if amt <= 50:
    #         return super().withdraw(amt)
    #     else:
    #         return False
    
    def withdraw (self, amt, guardian = None): # Q2b
        if guardian == self._guardian or amt <= 50:
            return super().withdraw(amt)
        else:
            return False
        
    def accumulateInterest(self): # overriding by refinement
        extraInt = 0.01 * self._balance
        super().accumulateInterest()
        self.deposit(extraInt)
    
    def __str__(self): # overriding by refinement
        return f'{super().__str__()} Guardian: {self._guardian}'

def q1q2():
    ja1 = JuniorAccount('JA1', 'Father', 100)
    print (ja1)
    ja1.accumulateInterest()
    print (ja1)
    ja1.withdraw (55, 'Father')
    print (ja1)
# q1q2()


class MovieCard:
    '''models a movie card
    has 2 attributes: price (float) and tickets (int)
    it has property method for tickets
    it has mutator method redeemTicket()
    it has __str__() method'''
    
    def __init__(self, price):
        self._price = price
        if price == 100:
            self._tickets = 15
        else:
            self._tickets = 10
        
    @property
    def tickets (self): 
        return self._tickets
    
    def __str__(self):
        return f'Ticket price: ${self._price} Tickets remaining: {self._tickets}'
    
    def redeemTickets(self, qty):
        if qty <= 2 and qty <= self._tickets:
            self._tickets -= qty
            return True
        else:
            return False
        
class HSBCMovieCard(MovieCard):
    '''subclass of MovieCard
    it has one additional attribute: name of CC holder
    it overrides redeemTicket() and __str__()'''
    
    def __init__(self, price, name):
        super().__init__(price)
        self._name = name
        self._tickets += 2
        
    def redeemTickets(self, qty = 1): # overriding by replacement
        if qty <= 4 and qty <= self._tickets:
            self._tickets -= qty
            return True
        else:
            return False
    
    def __str__(self):
        return f'{super().__str__()} Name: {self._name}'
    
def q3q4():
    mc1 = MovieCard(100)
    mc2 = MovieCard(70)
    print (mc1)
    print (mc2)
    mc1.redeemTickets(2)
    mc2.redeemTickets(3)
    print (mc1)
    print (mc2)
    hmc1 = HSBCMovieCard(100, 'Alex')
    hmc2 = HSBCMovieCard(70, 'Zoey')
    print (hmc1)
    print (hmc2)
    hmc1.redeemTickets(4)
    print (hmc1)
# q3q4()


from abc import ABC, abstractmethod

class Vehicle(ABC):
    '''this is an abstract class
    it has two attributes: vehNo and capacity
    it has abstract method: computeRoadTax()
    it has __str__() method'''
    
    def __init__(self, vehNo, cap):
        self._vehNo = vehNo
        self._cap = cap
        
    @property
    def vehNo(self):
        return self._vehNo
    @property
    def cap(self):
        return self._cap
    
    def computeRoadTax(self):
        pass
    
    def __str__(self):
        return f'Vehicle Number: {self._vehNo} | Capacity: {self._cap} | Road Tax: ${self.computeRoadTax():.2f}'
    
class PassengerVehicle(Vehicle):
    '''subclass of Vehicle
    it has two additional attributes: owner and age
    it overrides computeRoadTax()'''
    
    def __init__(self, vehNo, cap, owner, age):
        super().__init__(vehNo, cap)
        self._owner = owner
        self._age = age
    
    def computeRoadTax(self):
        rate = 1
        if self._age <= 55:
            tax = self._cap * rate
        else:
            tax = self._cap * 0.9 # 10% discount
        return tax
    
    def __str__(self):
        return f'Owner: {self._owner} | Age: {self._age} | {super().__str__()}'
    
class CommercialVehicle(Vehicle):
    '''subclass of Vehicle
    it has 2 additional attributes: company registration number (str) and maxLadenWeight (int)
    it overrides computeRoadTax()'''
    
    def __init__(self, vehNo, cap, CRN, MLW):
        super().__init__(vehNo, cap)
        self._CRN = CRN
        self._MLW = MLW
        
    def computeRoadTax(self):
        if self._MLW <= 3:
            tax = self._cap
        else:
            tax = self._cap * 1.5
        return tax
            
    def __str__(self):
        return f'Company registration number: {self._CRN} | {super().__str__()}'
        
def q5():
    pv1 = PassengerVehicle('pa111', 1500, 'Tim', 45)
    # print (pv1)
    pv2 = PassengerVehicle('pa222', 2300, 'Mike', 56)
    # print (pv2)
    company = CommercialVehicle('PA123', 2000, '1234', 4)
    # print (company)
    veh_list = [pv1, pv2, company]
    for n in veh_list:
        print (n)
# q5()


from datetime import datetime, date

class Flight:
    def __init__(self, flightNo, destination, departureDate, fare): 
        self._flightNo = flightNo
        self._destination =destination
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
                   
def q6():
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
q6()