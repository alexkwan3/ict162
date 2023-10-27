def q1a():
    '''70 is the price, and that will buy 10 tickets. card1.tickets will return 10, as the dictionary value of key 70 is 10'''
    
def q1b():
    '''it is missing the constructor for self._tickets
    this error occurs because it is calling the parent class's ticket property instead
    to have the correct output of 18, add the line below to the constructor:
    self._tickets = HSBCMovieCard._TICKET_COUNT[price]
    this will call the class variable in HSBCMovieCard instead'''
    
def q1c():
    '''proper way to call a setter method would be card1.tickets(11)
    however this won't work as the property is the same as setter.
    this can be resolved by changing either the property or setter name.
    in this case we can change the setter name to setTickets,
    and to call the setter, card1.setTickets(11), which will change self._tickets from 10 to 11'''

def q1d():
    '''add a function to the MovieCard and HSBCMovieCard class to add to the class variable'''
    # under MovieCard class:
    def addOffer(cost, qty): # does not need self as it is a class variable
        MovieCard._TICKET_COUNT[cost] = qty
        
    # under HSBCMovieCard Class:
    def addOffer(cost, qty):
        HSBCMovieCard._TICKET_COUNT[cost] = qty

class MovieCard:
    _TICKET_COUNT = {70:10, 100:15}
    def __init__(self, price):
        # assuming the price must either be 70 and 100
        self._price = price
        self._tickets = MovieCard._TICKET_COUNT[price]
    def setTickets(self, newTickets):
        self._tickets = newTickets
    def addOffer(cost, qty): # does not need self as it is a class variable
        MovieCard._TICKET_COUNT[cost] = qty
    @property
    def tickets(self):
        return self._tickets
    def __str__(self):
        return "Ticket value: ${:.2f} \t Tickets remaining: {}".format(self._price, self._tickets)
    
class HSBCMovieCard(MovieCard):
    _TICKET_COUNT = {70:12, 100:18}
    def __init__(self, name, price):
        super().__init__(price)
        self._name = name
        self._tickets = HSBCMovieCard._TICKET_COUNT[price]
    def addOffer(cost, qty):
        HSBCMovieCard._TICKET_COUNT[cost] = qty
    def __str__(self):
        """ string representation of the object """
        return "CardHolder Name: {}\t".format(self._name) + super().__str__()
    
def q1():
    card1 = MovieCard(70)
    print (card1.tickets)
    card2 = HSBCMovieCard('Alex Kwan', 100)
    print (card2.tickets)
    card1.setTickets(11)
    print (card1.tickets)
    MovieCard.addOffer(35, 5)
    HSBCMovieCard.addOffer(35, 6)
    card3 = MovieCard(35)
    card4 = HSBCMovieCard('Alex', 35)
    print (card3)
    print (card4)
# q1()

from abc import ABC, abstractmethod

class FoodItem(ABC):
    '''
    represents a food item
    has 2 instance variables: name (str) and cost (float)
    has property methods for _name and _cost
    has an abstract method expiryHours()
    has __str__() method'''
    
    def __init__(self, name, cost):
        self._name = name
        self._cost = cost
    
    @property
    def name (self): return self._name
    
    @property
    def cost (self): return self._cost
    
    @abstractmethod
    def expiryHours(self):
        pass
    
    def __str__(self):
        return f'Name: {self._name} Price: ${self._cost:.2f} Expiring in {self.expiryHours()} hours'

class Sandwich(FoodItem):
    '''subclass of FoodItem
    1 additional instance variable: fillings(str)'''
    
    def __init__(self, name, cost, fillings):
        super().__init__(name, cost)
        self._fillings = fillings
    
    def expiryHours(self):
        return 2
    
class HotSandwich(Sandwich):
    '''subclass of Sandwich
    has 1 additional instance variable: toasted (bool)'''
    
    def __init__(self, name, cost, fillings, toasted):
        super().__init__(name, cost, fillings)
        self._toasted = toasted
        
    def expiryHours(self):
        if self._toasted is True:
            return 1.5
        else:
            return super().expiryHours()
        
class Dessert(FoodItem):
    '''subclass of FoodItem
    has 1 additional variable: storageTemp(str)'''
    
    def __init__(self, name, cost, storageTemp):
        super().__init__(name, cost)
        self._storageTemp = storageTemp
    
    def expiryHours(self):
        if self._storageTemp <= 10:
            return 0.5
        elif self._storageTemp <= 20:
            return 1
        else:
            return 1.5
    
def q2():
    food1 = HotSandwich('Toasted Cheese Sandwich', 3.90, 'Toasted Cheese', True)
    food2 = HotSandwich('Hot Pastrami Sandwich', 4.80, 'Hot Pastrami', False)
    food3 = Sandwich('Cold Cut Sandwich', 4.50, 'Turkey Bacon')
    print (food1)
    print (food2)
    print (food3)
    # q2c: overriding by refinement for both, as i called the super class but also added on.
    # q2d(ii): 1.5 hours as it is toasted
# q2()

class SnackBoxException(Exception):
    '''subclass of Exception'''
    
class SnackBox:
    '''represents a snack box with selected FoodItems
    has 2 class variables: _MIN_ITEMS and _MAX_ITEMS
    has 4 instance variables: name (str), foodItems(dict), price(float), and consumeBy(float)
    has property methods for name, price, and consumeBy
    has mutator methods: removeItem() and addItem()
    has __str__() method'''
    
    _MIN_ITEMS = 1
    _MAX_ITEMS = 4
    
    def __init__(self, name:str, foodItem:FoodItem):
        self._name = name
        self._foodItems = {}
        self._price = foodItem.cost
        self._consumeBy = foodItem.expiryHours()
        self._foodItems[foodItem.name] = [self._price, self._consumeBy]
        
    @property
    def name (self): return self._name
    
    @property
    def price (self): return self._price
    
    @property
    def consumeBy (self): return self._consumeBy
    
    def addItem(self, item:FoodItem):
        if len(self._foodItems) < 4:
            self._foodItems[item.name] = [item.cost, item.expiryHours()]
        else:
            raise SnackBoxException (f'Error! Cannot have more than {SnackBox._MAX_ITEMS} items in snack box')
    
    def removeItem(self, name:str):
        if name not in self._foodItems.keys():
            raise SnackBoxException (f'Error! No such item ({name}) in snack box.')
        elif len(self._foodItems) == 1:
            raise SnackBoxException (f'Error! Must have at least {SnackBox._MIN_ITEMS} item in snack box.')
        else:
            del self._foodItems[name]
            
    def __str__(self):
        txt = ''
        total_cost = 0
        expiry = self._consumeBy
        for k, v in self._foodItems.items():
            txt += f'{k}, '
            total_cost += v[0]
            if v[1] < expiry:
                expiry = v[1]   
        return f'Name: {self._name} Price: ${total_cost:.2f} Consume in {expiry} hours\n' +\
            f'with {txt[:-2:]}'
            
def q3():
    chendol = Dessert('Chendol', 3.50, 4)
    chengteng = Dessert('Cheng Teng', 3.20, 16)
    icekachang = Dessert('Ice Kachang', 3.50, 4)
    puluthitam = Dessert('Pulut Hitam', 3.50, 38)
    bubur = Dessert('Bubur Cha Cha', 4.20, 38)
    
    try:
        sb1 = SnackBox('His Desserts', chendol)
        sb1.addItem(chengteng)
        sb1.addItem(icekachang)
        sb1.addItem(puluthitam)
        sb1.addItem(bubur)
    except SnackBoxException as sbe:
        print (sbe)
    finally:
        print (sb1)
    print ()
    try:
        sb2 = SnackBox('Her Desserts', chengteng)
        sb2.removeItem('Cheng Teng')
    except SnackBoxException as sbe:
        print (sbe)
    finally:
        print (sb2)
        
    # q3c: i used a dictionary as 
    # 1. it allowed me to assign the cost and expiry hours to each food item
    # 2. it is easier to manipulate to print out the str method
    '''q3d(v): the output will be:
    Error! Cannot have more than 4 items in snack box
    Name: His Desserts Price: $13.70 Consume in 0.5 hours
    with Chendol, Cheng Teng, Ice Kachang, Pulut Hitam
    
    Error! Must have at least 1 item in snack box.
    Name: Her Desserts Price: $3.20 Consume in 1 hours
    with Cheng Teng'''
# q3()
from tkinter import *
import tkinter as tk
from tkinter import ttk, scrolledtext

class ResultGUI:
    
    _classdict = { 'TMA': 
                {'Pass': ['G123123','E223344'], 
                 'Fail': ['E177890','M563746'],
                 'In Progress': ['M998877','G432432'] },
                  
                 'TOA': 
                {'Pass': ['E223344'],
                 'Fail': ['G123123'],
                 'In Progress': ['E177890','M563746','M998877','G432432'] } }
    
    def __init__(self):
        self._win = tk.Tk()
        self._win.geometry('380x300')
        self._win.title('ICT162 Result Enquiry')
        self.create_widgets()
        self._win.mainloop()
        
    def create_widgets(self):
        # create widgets
        self._studentID = tk.StringVar()
        self._lblId = ttk.Label(text='Student Id:')
        self._txtId = ttk.Entry(width=20, textvariable=self._studentID)
        self._rbtn = tk.IntVar()
        radioFrame = ttk.Frame(self._win)
        radioFrame.grid(row = 1, column = 1) # groups the radio buttons together
        self._rbtnAm = ttk.Radiobutton(radioFrame, text='TMA', value = 0, variable=self._rbtn)
        self._rbtnPm = ttk.Radiobutton(radioFrame, text='TOA', value = 1, variable=self._rbtn)
        btnFrame = ttk.Frame(self._win)
        self._btnEnquire = ttk.Button(btnFrame, text='Enquire',command=self.enquire)
        self._btnClear = ttk.Button(btnFrame, text='Clear', command = self.clear)
        self._sclText = scrolledtext.ScrolledText(width=35, height=4)
        self._sclText.config(state=tk.DISABLED)
        self._txtId.focus()
        # Placing the widgets using Grid layout manager
    #q4a:
        self._lblId.grid(row=0, column=0)
        self._txtId.grid(row=0, column=1)
        self._rbtnAm.grid(row=1, column=0)
        self._rbtnPm.grid(row=1, column=1)
        self._btnEnquire.grid(row=2, column=0)
        self._btnClear.grid(row=2, column=1)
        btnFrame.grid(row=2, column=1)
        self._sclText.grid(row=4, column=1)

    #q4c:
    def clear(self):
        self.create_widgets()
        self._win.mainloop()
        
    def enquire(self):
        assignment = self._rbtn.get()
        if assignment == 0:
            key = 'TMA'
        else:
            key = 'TOA'
        self._sclText.config(state=tk.NORMAL)
        student = self._studentID.get()
        txt = ''
        if student == '':
                txt = 'Enter Student ID and try again.'
        else:
            for k, v in ResultGUI._classdict[key].items():
                    if student in v:
                        txt = f'{key} result for ICT162: {k}'
                        break
        if txt == '':
            txt = 'You did not enroll for ICT162.'
        self._sclText.insert(tk.END, txt + '\n')
            
ResultGUI()

def q4b():
    '''it should be inserted after line 4 as a class variable'''
    
