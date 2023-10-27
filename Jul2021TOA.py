def q1a():
    '''
    _winningPoints is a class variable in the Game class. 
        This is a class variable because it is used multiple times in the class and it is modular with the setWinningPoints method.
    _players is a class variable dictionary in the Game class storing the player ID and name as key and value.
        A dictionary allows the user to easily locate or refer to each player by the player ID (key).
    setWinningPoints is a class method in the Game class for changing the class variable _winningPoints.
        This allows _winningPoints to be modular and easily changed.
    deductPlayerPoints locates the player and deducts the points by the provided number.
        This is a mutator method as it allows the user to deduct the points for a chosen player.
    '''
    
class Player:
    
    _currentID = 0
    
    def __init__(self):
        Player._currentID += 1
        self._ID = Player._currentID
        self._points = 5
        self._active = True
        
    @property
    def ID (self): return self._ID
    
    @property
    def points(self): return self._points
    
    @property
    def active (self): return self._active
    
    @points.setter
    def points (self, newPoints):
        if newPoints <= 0: 
            self._points = 0
            self._active = False
        else:
            self._points = newPoints
            
    def __str__(self):
        return f'ID: {self._ID}, Points: {self._points}, Active: {self._active}'
    
class Game:
    
    _gamePoints = 3
    _winningPoints = 15
    
    def __init__(self):
        self._players = {}
        
    @classmethod
    def winningPoints(cls): return Game._winningPoints
    
    @classmethod
    def setWinningPoints (cls, newPoints):
        Game._winningPoints = newPoints
        
    def deductPlayerPoints(self, pID):
        if pID not in self._players.keys():
            return False
        else:
            self._players[pID].points -= Game._gamePoints
            return True
    
    def getWinners(self):
        winlist = []
        for k, v in self._players.items():
            if v.points >= Game._winningPoints:
                winlist.append(k)
        return winlist
    
    def addPlayer(self, player):
        if player.ID not in self._players.keys():
            self._players[player.ID] = player
            return True
        else:
            return False
        
    def removePlayer(self, pID):
        if pID in self._players.keys():
            p = self._players.pop(pID)
            return p
        else:
            return None
        
    def getPlayer(self, pID):
        if pID in self._players.keys():
            return self._players[pID]
        else:
            return None
        
    def __str__(self):
        txt = 'Game Player List:\n'
        for v in self._players.values():
            txt += f'ID: {v.ID}, Points: {v.points}, Active: {v.active}\n'
        return txt
    
def q1():
    game = Game()
    p = Player()
    p.points = 15
    # game.addPlayer(p)
    if game.addPlayer(p) is True:
        print ('Successfully added')
    else:
        print ('Unable to add')
    game.setWinningPoints(12)
    game.deductPlayerPoints(1)
    print (game)
    print (game.getWinners())
# q1()

from abc import ABC, abstractmethod
from datetime import *
from datetime import datetime

class Pet(ABC):
    
    def __init__(self, ID, name, DOB:datetime, owner = None):
        self._ID = ID
        self._name = name
        self._DOB = DOB
        self._owner = owner
        
    @property
    def ID (self): return self._ID
    
    @property
    def DOB (self): return self._DOB
    
    @property
    def owner (self): return self._owner
    
    @property
    def address (self):
        if self._owner is not None:
            return self._owner.address
        else:
            raise PetAgencyException ('Pet has no owner.') # q3b
    
    @owner.setter
    def owner (self, newOwner):
        self._owner = newOwner
        
    @address.setter
    def address (self, newAddress):
        if self._owner is not None:
            self._owner.address = newAddress
        else:
            raise PetAgencyException ('Pet has no owner.') # q3b
        
    @abstractmethod
    def ageInHumanYears(self):
        pass
    
    def hdbFriendly(self):
        return False
    
    def __str__(self):
        if self._owner is not None:
            return f'ID: {self.ID}\tHDB Friendly: {self.hdbFriendly()}\n' +\
                f'Name: {self._name}\tDOB: {self.DOB:%d-%b-%Y}\tAge in human years: {self.ageInHumanYears()}\n' +\
                    f"Owner's name: {self._owner.name}\tAddress: {self.address}"
        else:
            return f'ID: {self.ID}\tHDB Friendly: {self.hdbFriendly()}\n' +\
                f'Name: {self._name}\tDOB: {self.DOB:%d-%b-%Y}\tAge in human years: {self.ageInHumanYears()}'
                
class Dog(Pet):
    
    def __init__(self, ID, hdbFriendly, name, DOB, owner=None):
        super().__init__(ID, name, DOB, owner)
        self._hdbFriendly = hdbFriendly
        
    def ageInHumanYears(self):
        petAge = date.today() - self._DOB
        petAge = petAge.days / 365.25
        if petAge <= 1:
            return 15
        elif petAge <= 2:
            return 24
        else:
            humanAge = (petAge - 2) * 5 + 24
            return round(humanAge)
    
    def hdbFriendly(self):
        return self._hdbFriendly
    
    def __str__(self):
        return f'Dog {super().__str__()}'
    
class PetOwner: # for testing
    
    def __init__(self, name, address):
        self._name = name
        self._address = address
        
    @property
    def name(self): return self._name
    
    @property
    def address(self): return self._address
    
    @address.setter
    def address(self, newAddress):
        self._address = newAddress
        
    def __str__(self):
        return f'Name: {self._name}\tAddress: {self._address}'
    
def q2():
    '''
    q2(a)
    (i): Object composition. The Pet class is composed of the Owner class.
    (ii): Inheritance. The Cat class is a subclass of the Pet class and inherits from the Pet class.
    '''
    
    alex = PetOwner('Alex', 'Hougang')
    d1 = date(2019, 4, 17)
    jovie = Dog('S1234', 'Jovie', d1, alex)
    jovie.address = 'Admiralty'
    print (jovie)
# q2()

class Cat(Pet):
    
    def __init__(self, ID, name, DOB: datetime, owner=None):
        super().__init__(ID, name, DOB, owner)
        
    def ageInHumanYears(self):
        petAge = date.today() - self._DOB
        petAge = petAge.days / 365.25
        if petAge <= 1:
            return 19
        elif petAge <= 2:
            return 24
        else:
            humanAge = (petAge - 2) * 4 + 24
            return round(humanAge)
        
    def hdbFriendly(self):
        return False
    
    def __str__(self):
        return f'Cat {super().__str__()}'

class PetAgencyException(Exception):
    '''subclass of Exception
    raised when there is a business rule violation'''
    
class PetAdoptionAgency:
    
    def __init__(self):
        self._pets = []
        
    def searchPet(self, id):
        for n in self._pets:
            if n.ID == id:
                return n
        return None
    
    def addPet(self, pet):
        if self.searchPet(pet.ID) is None:
            self._pets.append(pet)
            return True
        else:
            raise PetAgencyException (f'Duplicate pet identification ({pet.ID}). Cannot add.')
        
    def adopt(self, owner, id):
        adoptcount = 0
        i = -1
        for n in range (len(self._pets)):
            if self._pets[n].owner == owner and self._pets[n].address == owner.address:
                adoptcount += 1
                if adoptcount == 2:
                    raise PetAgencyException ('Owner has adopted 2 pets already. Adoption quota reached.')
            if self._pets[n].ID == id:
                if self._pets[n].owner is None:
                    i = n
                else:
                    raise PetAgencyException ('Pet already has an owner. Cannot be adopted.')
        if i == -1:
            raise PetAgencyException (f'Incorrect pet identification ({id}). Cannot adopt.')
        else:
            self._pets[i].owner = owner
            return True
        
    def updateAddress(self, id, address):
        for n in range (len(self._pets)):
            if self._pets[n].ID == id:
                self._pets[n].address = address
                return True
        raise PetAgencyException (f'Incorrect pet identification ({id}). Cannot update address.')
    
    def __str__(self):
        txt = ''
        for n in self._pets:
            txt += f'{n}\n'
        return txt
    
def q3():
    d1 = date (2019, 12, 7)
    d2 = date (2018, 1, 12)
    jackie = Dog('D123', True, 'Jackie', d1)
    sparkle = Cat('C031', 'Sparkle', d2)
    peter = PetOwner('Peter', '12 Dunbar Road')
    ginger = Cat('C017', 'Ginger', d2, peter)
    agency = PetAdoptionAgency()
    agency.addPet(jackie)
    agency.addPet(sparkle)
    agency.addPet(ginger)
    while True:
        try:
            choice = input ('Menu\n'+\
            '1. Update pet address\n'+\
                '2. Adopt a pet\n'+\
                    '0. Exit\n'+\
                        'Enter a choice: ')
            if choice.isdigit() is False:
                print ('Please enter a number for menu choice.')
            elif choice == '0':
                print ('Application ends')
                break
            elif choice == '1':
                id = input ('Enter pet ID: ').upper()
                newAddress = input ('Enter new address: ')
                agency.updateAddress(id, newAddress)
            elif choice == '2':
                name = input ("Enter owner's name: ")
                add = input ("Enter address: ")
                newOwner = PetOwner(name, add)
                id = input ('Enter pet ID: ').upper()
                agency.adopt(newOwner, id)
            else:
                print ('Invalid option, please choose again.')
        except PetAgencyException as p:
            print (p)
# q3()

import tkinter as tk
from tkinter import ttk, scrolledtext as st
class PetAgeCalculatorGui:
    def __init__(self):
        self._win = tk.Tk() 
        self._win.resizable(False, False)
        self.create_widgets() 
        self._win.geometry('400x200') 
        self._win.mainloop()
    
    def create_widgets(self):
        dataFrame = ttk.Frame(self._win)
        self._age_lbl = ttk.Label(dataFrame, text="Age:") 
        self._age_lbl.grid(column = 0, row = 0) #q4a
        self._ageValue_Ety = ttk.Entry(dataFrame, width=18)
        self._ageValue_Ety.grid(column=1, row=0, sticky=tk.EW)
        for_lbl = ttk.Label(dataFrame, text="For")
        for_lbl.grid(column=0, row=1)
        radioFrame = ttk.Frame(dataFrame)
        radioFrame.grid(column=1, row=1, sticky=tk.EW)
        self._rbtn = tk.IntVar()
        cat_rdbtn = tk.Radiobutton(radioFrame, text = 'Cat', value = 0, variable = self._rbtn) #q4b
        dog_rdbtn = tk.Radiobutton(radioFrame, text = 'Dog', value = 1, variable = self._rbtn) #q4b
        cat_rdbtn.grid(column=1, row=0, sticky=tk.W) 
        dog_rdbtn.grid(column=2, row=0, sticky=tk.W)
        actionFrame = ttk.Frame(dataFrame)
        actionFrame.grid(column=1, row=3)
        self._convert_btn = ttk.Button(actionFrame, text="To Human Years", command = self.convert)
        self._convert_btn.pack(side=tk.LEFT) 
        self._clear_btn = ttk.Button(actionFrame, text="Clear", command = self.clear) 
        self._clear_btn.pack(side = tk.LEFT) # q4a
        self._output_lbl = ttk.Label(dataFrame, text=f"Output:",justify=tk.LEFT)
        self._output_lbl.grid(column=0, row=4, columnspan = 2, sticky=tk.EW) 
        dataFrame.pack(side = tk.TOP)
    #q4b:
        self._sclText = st.ScrolledText(width=35, height=10)
        self._sclText.config(state=tk.DISABLED)
        self._sclText.pack(side=tk.BOTTOM)
        self._ageValue_Ety.focus()
        
    #q4b:
    def clear(self):
        self._sclText.config(state=tk.NORMAL)
        self._ageValue_Ety.delete(0, tk.END)
        self._sclText.delete(1.0, tk.END)
        self._sclText.config(state=tk.DISABLED)
        self._ageValue_Ety.focus()
        self._rbtn.set(0) # selects radio button
    
    def convert(self):
        self._sclText.config(state=tk.NORMAL)
        age = int (self._ageValue_Ety.get())
        animal = self._rbtn.get()
        if animal == 0:
            type = 'Cat'
            if age <= 1:
                humanAge = 19
            elif age <= 2:
                humanAge = 24
            else:
                humanAge = (age - 2) * 4 + 24
        else:
            type = 'Dog'
            if age <= 1:
                humanAge = 15
            elif age <= 2:
                humanAge = 24
            else:
                humanAge = (age - 2) * 5 + 24
        txt = f'{type} {age} years = {humanAge} human years'
        self._sclText.insert(tk.END, txt + '\n')
        
# PetAgeCalculatorGui()