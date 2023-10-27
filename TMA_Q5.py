from tkinter import *
import tkinter.scrolledtext as st
from datetime import *
from guest import *

class ReasonException(Exception):
    '''subclass of Exception
    used when no Reason provided for blacklist'''

class Q5(Frame):
    '''subclass of Frame'''
    
    def __init__(self):
        Frame.__init__(self)
        self.master.title ('SAMI Blacklist GUI - done by Alexandre')
        self.master.geometry ('800x400')
        self._guests = self.setupGuests()
        self.create()
        self.layout()
    
    def create(self):
        self._lbPP = Label (self, text = 'Passport: ')
        self._lbDateReported = Label (self, text = 'Date Reported: ')
        self._lbddmonyyyy = Label (self, text = '(dd-mon-yyyy)')
        self._lbReason = Label (self, text = 'Reason(s): ')
        
        self._btnSearch = Button (self, text = 'Search', command = self.search)
        self._btnBlacklist = Button (self, text = 'Blacklist', command = self.blacklist)
        self._btnReset = Button (self, text = 'Reset', command = self.reset)
        
        self._etyPP = Entry (self, width = 10)
        self._etyDateReported = Entry (self, width = 10)
        self._etyReason = Entry (self, width = 10)
        
        self._stText = st.ScrolledText (self, width = 60, height = 20)
        
        self._btnBlacklist.configure(state = 'disabled')
        self._btnReset.configure(state='disabled')
        self._stText.configure(state='disabled')
        self._etyDateReported.configure(state='disabled')
        self._etyReason.configure(state='disabled')
    
    def setupGuests(self):
        guests = {}
        infile = open("Guests.txt", "r") 
        for line in infile:
            pp,name,country = line.split(",")
            guests[pp.strip()] = Guest(pp.strip(),name.strip(),country.strip()) 
        infile.close()
    
        infile = open("Blacklist.txt", "r")
        for line in infile:
            pp, dateReported, reason = line.split(",") 
            g = guests.get(pp.strip())
            if g is not None:
                g.blacklist(datetime.strptime(dateReported.strip(), "%d-%b-%Y").date(), reason.strip())
        infile.close()
        return guests
        
    def search(self):
        self._ppNo = self._etyPP.get()
        if self._ppNo not in self._guests.keys():
            txt = 'Unable to locate a guest with this passport number.'
        else:
            txt = f'{self._guests[self._ppNo]}\nEnter date and reason to blacklist...'
            self._etyPP.configure(state = 'disabled')
            self._btnSearch.configure(state = 'disabled')
            self._etyDateReported.configure(state = 'normal')
            self._etyReason.configure(state = 'normal')
            self._btnBlacklist.configure(state = 'normal')
        self._stText.configure(state = 'normal')
        self._stText.insert(END, txt + '\n')
        self._btnReset.configure(state = 'normal')
        
    def blacklist(self):
        dateReported = self._etyDateReported.get()
        try:
            dateReported = datetime.strptime(dateReported, '%d-%b-%Y').date()
            reason = self._etyReason.get()
            if reason == '' or reason.isspace() == True:
                raise ReasonException
            self._guests[self._ppNo].blacklist(dateReported, reason)
            txt = f'{self._guests[self._ppNo]}'
            self._stText.insert(END, txt)
            fw = open ('Blacklist.txt', 'w')
            for n in self._guests.values():
                for i in n._blacklistedReason:
                    print (f'{n._passport}, {i[0]:%d-%b-%Y}, {i[1]}', file = fw)
            fw.close()
        except ValueError as ve:
            ve = 'Please enter date in dd-mon-yyyy format....\n'
            self._stText.insert(END, ve)
        except ReasonException as re:
            re = 'Please enter reason.\n'
            self._stText.insert(END, re)
            
    def reset(self):
        self.create()
        self.layout()
        # self._etyPP.focus_set() # redundant as layout() already has this line
            
    def layout(self):
        self._lbPP.grid(row = 0, column = 0)
        self._etyPP.grid(row = 0, column = 1)
        self._lbDateReported.grid(row = 1, column = 0)
        self._lbddmonyyyy.grid(row = 1, column = 2)
        self._etyDateReported.grid(row = 1, column = 1)
        self._lbReason.grid(row = 2, column = 0)
        self._etyReason.grid(row = 2, column = 1)
        self._btnSearch.grid(row = 3, column = 0)
        self._btnBlacklist.grid(row = 3, column = 1)
        self._btnReset.grid(row = 3, column = 2)
        self._stText.grid(row = 4, column = 0, columnspan = 4)
        self._etyPP.focus_set()
        
        self.pack()
            
def q5():
    app = Q5()
    app.mainloop()
q5()