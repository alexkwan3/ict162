class Person:
    '''models a person
    it has 3 attributes: gender (str), name(str), lastName (str)
    it has property methods for gender, name, lastName
    it has setter method for name
    it has accessor methods: getFullname() and getInitials()
    it has __str__() method'''
    
    def __init__(self,gender,name,lastName):
        self._gender = gender
        self._name = name
        self._lastName = lastName
        
    @property
    def gender(self): return self._gender
    @property
    def name(self): return self._name
    @property
    def lastName(self): return self._lastName
    @name.setter
    def name(self,newName): self._name = newName
    
    def getFullName(self):
        salute = 'Mr.'
        if self._gender == 'F':
            salute = 'Ms.'
        return f'{salute} {self._lastName} {self._name}'
    
    def getInitials(self):
        return f'{self._name[0]}. {self._lastName}'

    def __str__(self):
        txt = 'Male'
        if self._gender == 'F':
            txt = 'Female'
        return f'Name: {self._name} {self._lastName} Gender: {txt}'
    

def q1():
    p = Person ('M', 'Joe', 'Lee')
    print (p)
    p2 = Person('F', 'Amy', 'Tan')
    print (p2)
    print (p.getFullName())
    print (p2.getInitials())
# q1()


class Rectangle:
    '''models a rectangle
    it has 2 attributes: length (float), width (float)
    it has property methods for length and width
    it has setter methods for length and width
    it has accessor methods: getArea(), getPerimeter(), isBigger()
    it has mutator method: increaseSize()
    it has __str__()'''
    
    def __init__(self, length, width):
        self._length = length
        self._width = width
        
    @property
    def length(self): return self._length
    @property
    def width(self): return self._width
    @length.setter
    def length(self,newLength): self._length = newLength
    @width.setter
    def width(self,newWidth): self._width = newWidth
    
    def getArea(self):
        area = self._length * self._width
        return area
    
    def getPerimeter(self):
        perimeter = self._length * 2 + self._width * 2
        return perimeter
    
    def increaseSize(self,deltaLength,deltaWidth):
        self._length += deltaLength
        self._width += deltaWidth
        
    def isBigger(self, otherRect):
        '''accepts another Rectangle object, otherRect
        compares area of this rectangle with other rectangle, otherRect
        returns True if this area is bigger; otherwise returns False'''
        if self.getArea() > otherRect.getArea():
            return True
        return False
    
    def __str__(self):
        return f'Length: {self._length:.1f} Width: {self._width:.1f} Area: {self.getArea():.1f} Perimeter: {self.getPerimeter():.1f}'
    
def q2():
    r = Rectangle(2, 4)
    print (r)
    r.increaseSize(0.5, 0.7)
    print (r)
    r2 = Rectangle (2,3)
    print (r2)
    if r.isBigger(r2):
        print ('r is bigger')
    else:
        print ('r is smaller')        
# q2()


class BankAccount:
    '''models a bank account
    it has 3 attributes: accountID (str), pin (int), balance (float)
    it has property methods for accountID, pin, balance
    it has setter methods balance
    it has mutator methods: changePin(), deposit(), withdraw(), transferTo()
    it has __str__()
    '''
    
    def __init__(self,id,pin,amt):
        self._id = id
        self._pin = pin
        self._balance = amt
        
    def __str__(self):
        return (f'ID: {self._id} Balance: ${self._balance:.2f}')
    
    @property
    def id(self): return self._id
    @property
    def pin(self): return self._pin
    @property
    def balance(self): return self._balance
    @balance.setter
    def balance(self,newAmt): self._balance = newAmt
    
    def changePin(self,oldPin,newPin):
        if oldPin == self._pin:
            self._pin = newPin
            print (f"PIN has been updated to {newPin}.")
            return True
        print ("PIN has not been updated. Current PIN is incorrect, please try again.")
        return False
    
    def deposit(self,amt):
        self._balance += amt
        
    def withdraw(self,amt):
        if amt <= self._balance:
            self._balance -= amt
            return True
        return False
    
    def transferTo(self,otherAcc,amt):
        '''accepts another bank account obejct, otherAcc and an amount to transfer
        attempts to transfer from this account to otherAcc the amt value
        returns true if successful, otherwise return False'''
        if self.withdraw(amt):
            otherAcc.deposit(amt)
            return True
        return False
    
def q4():
    ba = BankAccount('all', 123, 100)
    print (ba)
    ba2 = BankAccount('b22', 456, 200)
    print (ba2)
    ba.deposit(11)
    ba2.withdraw(55)
    print (ba)
    print (ba2)
    if ba.transferTo(ba2,22):
        print ('Successful transfer')
    else:
        print ('Not enough money')
    print (ba)
    print (ba2)
    ba2.changePin(456, 789)
# q4()

import math

class Point:
    '''models a 2D point (x,y)
    has 2 attributes: x (float), y (float)
    has property methods for x and y
    has setter methods for x and y
    has mutator methods move(), distanceTo(), quadrant()
    has __str__()'''
    
    def __init__(self, x = 0, y = 0):
        self._x = x
        self._y = y
    
    @property
    def x(self): return self._x
    @property
    def y(self): return self._y
    @x.setter
    def x(self, x): self._x = x
    @y.setter
    def y(self, y): self._y = y
    
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
        return self._x, self._y
    
    def distanceTo(self, pt):
        distance = math.sqrt((self._x - pt._x) ** 2 + (self._y - pt._y) ** 2)
        return distance
        
    def quadrant(self):
        if self._x == 0 or self._y == 0:
            return 0
        elif self._x > 0:
            if self._y > 0:
                return 1
            else:
                return 2
        else:
            if self._y > 0:
                return 4
            else:
                return 3
        
    def __str__(self):
        return f'({self._x}, {self._y})'
        
def q3():
    p1 = Point (5, 1)
    # p1 = Point(0, 0)
    # print (p1)
    # p1.x = 5
    # p1.y = 1
    print (p1)
    p1.move(5, -5)
    print (p1)
    p2 = Point (10, -10)
    # p2 = Point(0, 0)
    # p2.x = 10
    # p2.y = -10
    print (p2)
    print (f'The distance between point {p1} and point {p2} is {p1.distanceTo(p2):.2f}')
    print (p1.quadrant())
    print (p2.quadrant())
# q3()


class ToDo:
    '''models a to-do list
    has 2 attributes: event (str) and actions (list)
    has a property method for event (str)
    has mutator methods addToDo() and removeToDo()
    has __str__()'''
    
    def __init__(self, event):
        self._event = event
        self._actions = []
    
    @property
    def event(self): return self._event
    
    def addToDo(self, toDo):
        self._actions.append(toDo)
        return self._actions
    
    def removeToDo(self, index):
        if 1 <= index <= len(self._actions):
            del self._actions [index-1] # list index starts with 0
            return True
        return False
    
    def __str__(self):
        txt = f'Event: {self._event}\n'
        for i, a in enumerate(self._actions):
            txt += f'{i+1}. {a}\n'
        return txt
    
def q5():
    event = 'Orientation Camp'
    travel = ToDo(event)
    travel.addToDo('bring passport')
    travel.addToDo('change money')
    travel.addToDo('bring medicine')
    print (travel)
    travel.removeToDo(3)
    print (travel)
# q5()