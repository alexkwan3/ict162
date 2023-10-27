from abc import ABC, abstractmethod

class ClubHead(ABC):
    '''abstract class
    has 2 instance variables: loft (float) and weight (int)
    property method for weight
    has abstract method getHeight()
    has __str__() method'''
    
    def __init__(self, loft, weight):
        self._loft = loft
        self._weight = weight
        
    @property
    def weight (self): return self._weight
    
    @abstractmethod
    def getHeight(self):
        pass
    
    def __str__(self):
        return f'Loft: {self._loft} degrees\tWeight: {self._weight}g'
    
class WoodHead(ClubHead):
    '''subclass of ClubHead
    has 1 additional instance variable: size (int)
    has accessor method getHeight()
    has __str__() method'''
    
    def __init__(self, loft, weight, size):
        super().__init__(loft, weight)
        self._size = size
        
    def getHeight(self):
        height = self._size / 400
        return height
    
    def __str__(self):
        return f'{super().__str__()}\tHead Size: {self._size}cc'
    
class IronHead(ClubHead):
    '''subclass of ClubHead
    has 1 additional variable: material (str)
    has getHeight() method which returns 1 inch
    has __str__() method'''
    
    def __init__(self, loft, weight, material):
        super().__init__(loft, weight)
        self._material = material
      
    def getHeight(self):
        return 1
    
    def __str__(self):
        return f'{super().__str__()}\tMaterial: {self._material}'
    
class PutterHead(ClubHead):
    '''subclass of ClubHead
    has 1 additional variable: style(str)
    has getHeight() method
    has __str__() method'''
    
    def __init__(self, loft, weight, style):
        super().__init__(loft, weight)
        self._style = style
        
    def getHeight(self):
        if self._style == 'Blade':
            return 1
        else:
            return 0.5
        
    def __str__(self):
        return f'{super().__str__()}\tStyle: {self._style}'

def q1():
    putter = PutterHead(3.5, 365, 'Blade')
    iron = IronHead(37.5, 285, 'Forged')
    wood = WoodHead(9.5, 206, 450)
    print (f'{putter}\t\tHeight: {putter.getHeight()}\n{iron}\tHeight: {iron.getHeight()}\n{wood}\tHeight: {wood.getHeight()}')
# q1()

class Club:
    '''has 4 instance variables: label(str), head(ClubHead), shaft(Shaft), grip(Grip)
    has property method for label, length, weight
    has mutator method changeGrip()
    has __str__() method'''
    
    def __init__(self, label, head, shaft, grip):
        self._label = label
        self._head = head
        self._shaft = shaft
        self._grip = grip
        
    @property
    def label(self): return self._label
    
    @property
    def length(self):
        ln = self._shaft.length + self._head.getHeight()
        return ln
    
    @property
    def weight(self):
        wt = self._head.weight + self._shaft.weight + self._grip.weight
        return wt
    
    def changeGrip(self, newGrip): # newGrip is a Grip class object
        self._grip = newGrip
        
    def __str__(self):
        return f'Club: {self._label}\tLength: {self.length:.3f}in\tWeight: {self.weight}g'
    
class Shaft: # for testing
    '''models a golf club shaft
    has 4 instance variables: length (float), weight (int), material (str), flex (str)
    has property methods for length and weight'''
    
    def __init__(self, length, weight, material, flex):
        self._length = length
        self._weight = weight
        self._material = material
        self._flex = flex
        
    @property
    def length (self): return self._length
    
    @property
    def weight (self): return self._weight
    
class Grip: # for testing
    '''models a golf club grip
    has 3 instance variables: diameter (float), weight (int), material (str)
    has property method for weight'''
    
    def __init__(self, diameter, weight, material):
        self._diameter = diameter
        self._weight = weight
        self._material = material
        
    @property
    def weight (self): return self._weight
    
def q2(): # code won't run as Shaft & Grip classes are not written
    # q2b(i)
    currentGrip = Grip (0.6, 62, 'Rubber')
    newGrip = Grip (0.58, 65, 'Leather')
    driverHead = WoodHead(10.5, 203, 450)
    iron8Head = IronHead(34.5, 268, 'Cast')
    sunsetHead = PutterHead(3, 380, 'Mallet')
    driverShaft = Shaft (45, 65, 'Graphite', 'Stiff')
    iron8Shaft = Shaft (35.5, 109, 'Steel', 'Regular')
    sunsetShaft = Shaft (33, 120, 'Steel', 'Stiff')
    driver = Club('Driver', driverHead, driverShaft, currentGrip)
    iron8 = Club('8-Iron', iron8Head, iron8Shaft, currentGrip)
    sunset = Club('Sunset', sunsetHead, sunsetShaft, currentGrip)
    
    #q2b(ii):
    total_weight = driver.weight + iron8.weight + sunset.weight
    print (f'Total weight: {total_weight}g')
    
    #q2b(iii):
    driver.changeGrip(newGrip)
    iron8.changeGrip(newGrip)
    sunset.changeGrip(newGrip)
    
    print (driver)
    print (iron8)
    print (sunset)
    
    '''q2b(iv):
    Polymorphism is when a function or class can be used for different purposes.
    For example, the subclasses WoodHead, IronHead, and PutterHead are polymorphism through inheritance.
    Another example would be the Shaft and Grip classes being used to make different Shaft and Grip objects.
    
    q2c(i): Object composition. The Club class is composed of other classes, one of them being the Shaft class.
    (ii): Inheritance. The PutterHead class is a subclass of ClubHead, and inherits parts of ClubHead, such as the constructor and __str__() method.
    (iii): Object composition. The Club class is composed of other classes, in which IronHead would work as one of them being a ClubHead subclass.'''
# q2()

class GolfBag:
    '''models a golf bag
    has 3 instance variables: owner (str), weight (int), compartments (collection)
    has mutator methods: addClub() and removeClub()
    has accessor method: getTotalWeight()
    has __str__() method'''
    
    _max_clubs = 14 # q3c
    _max_weight = 7500 # q3c
    
    def __init__(self, owner, weight):
        self._owner = owner
        self._weight = weight
        self._compartments = []
        
    def addClub(self, club: Club):
        currentWeight = self.getTotalWeight()
        if currentWeight + club.weight <= GolfBag._max_weight:
            if len(self._compartments) < GolfBag._max_clubs:
                  self._compartments.append (club)      
            else:
                raise GolfEquipmentException (f'A maximum of {GolfBag._max_clubs} clubs is allowed.')
        else:
            raise GolfEquipmentException (f'Max Weight of {GolfBag._max_weight} exceeded.')
        
    def removeClub(self, lbl:str):
        for n in range (len(self._compartments)):
            if self._compartments[n].label == lbl:
                self._compartments.pop(n)
                return True
        return False
    
    def getTotalWeight(self):
        total_weight = self._weight
        for n in self._compartments:
            total_weight += n.weight
        return total_weight
    
    def __str__(self):
        txt = f'Golf Bag Owner: {self._owner}\n'
        for n in self._compartments:
            txt += f'Club: {n.label}\tLength: {n.length:.3f}in\tWeight: {n.weight}g\n'
        txt += f'Total weight: {self.getTotalWeight()}g'
        return txt
    
class GolfEquipmentException(Exception):
    '''subclass of Exception'''
    
def q3():
    bag = GolfBag('Alex', 1000)

    currentGrip = Grip (0.6, 62, 'Rubber')
    driverHead = WoodHead(10.5, 203, 450)
    iron8Head = IronHead(34.5, 268, 'Cast')
    sunsetHead = PutterHead(3, 380, 'Mallet')
    driverShaft = Shaft (45, 65, 'Graphite', 'Stiff')
    iron8Shaft = Shaft (35.5, 109, 'Steel', 'Regular')
    sunsetShaft = Shaft (33, 120, 'Steel', 'Stiff')
    driver = Club('Driver', driverHead, driverShaft, currentGrip)
    iron8 = Club('8-iron', iron8Head, iron8Shaft, currentGrip)
    sunset = Club('Sunset', sunsetHead, sunsetShaft, currentGrip)
    
    bag.addClub(driver)
    bag.addClub(iron8)
    bag.addClub(sunset)
    bag.removeClub('Driver')
    
    print (bag)
# q3()

def q3b():
    '''I chose to use a list as each club is an independent entity and there was no need for key-value pairs, hence a list made more sense.'''
    
import tkinter as tk
from tkinter import ttk, scrolledtext
class GolfDistanceCalculatorGUI: # to test
    def __init__(self):
        self._win = tk.Tk()
        self._win.title("Golf Distance Calculator") 
        self._win.resizable(True, True) 
        self._win.geometry("320x180") # resolution may differ
        self.create_widgets()
        self._win.mainloop()
        
    def create_widgets(self):
        dataFrame = ttk.Frame(self._win) 
        dataFrame.grid(column=0, row=0)
        swingSpeed_lbl = ttk.Label(dataFrame, text="Swing Speed (mph):") 
        swingSpeed_lbl.grid(column=0, row=0)
        actionFrame = ttk.Frame(dataFrame)
        actionFrame.grid(column=0, row=1, columnspan=2) 
        self._calculate_btn = ttk.Button(actionFrame, text="Calculate", command = self.calculate)
        
        self._swingspeed = tk.StringVar()
        self._etyswingspeed = ttk.Entry(dataFrame, width=5, textvariable=self._swingspeed)
        # by using dataFrame, it groups the label and entry together
        self._etyswingspeed.grid(column = 1, row = 0)

        self._calculate_btn.pack(side = tk.LEFT, padx=4, pady=4) 
        self._clear_btn = ttk.Button(actionFrame, text="Clear", command = self.clear) 
        self._clear_btn.pack(side = tk.LEFT, padx=4, pady=4)
        outputFrame = ttk.Frame(self._win)
        outputFrame.grid(column=0, row=4, columnspan=2) 
        self._scrol_stxt = scrolledtext.ScrolledText(outputFrame, width=35,height=5, wrap=tk.WORD)
        self._scrol_stxt.grid(column=0, row=5)
        # disabled to disallow data entry into scrolledText 
        self._scrol_stxt.config(state=tk.DISABLED)
        
        self._etyswingspeed.focus()
    
    def calculate(self):
        self._scrol_stxt.config(state=tk.NORMAL)
        swingspeed = self._swingspeed.get()
        if swingspeed.isdigit() is True and int(swingspeed) > 0:
            distance = int(swingspeed) * 2.6
            txt = f'Estimated distance: {distance:.0f} yards'
        else:
            txt = 'Error(s) in input values\nPlease <clear> and try again'
        self._scrol_stxt.insert(tk.END, txt + '\n')
            
    def clear(self):
        self.create_widgets()
        self._win.mainloop()

# GolfDistanceCalculatorGUI()

def q4b(): # insert under create_widgets(self)
    '''
    self._swingspeed = tk.StringVar()
    self._etyswingspeed = ttk.Entry(dataFrame, width=5, textvariable=self._swingspeed)
    self._etyswingspeed.grid(column = 0, row = 0)
    '''
    
def q4c():
    '''
    self._calculate_btn = ttk.Button(actionFrame, text="Calculate", command = self.calculate)
    self._clear_btn = ttk.Button(actionFrame, text="Clear", command = self.clear)
    
    def calculate(self):
        self._scrol_stxt.config(state=tk.NORMAL)
        swingspeed = self._swingspeed.get()
        if swingspeed.isdigit() is True and int(swingspeed) > 0:
            distance = swingspeed * 2.6
            txt = f'Estimated distance: {distance} yards'
        else:
            txt = 'Error(s) in input values\nPlease <clear> and try again'
        self._scrol_stxt.insert(tk.END, txt + '\n')
            
    
    def clear(self):
        self.create_widgets()
        self._win.mainloop()
    '''