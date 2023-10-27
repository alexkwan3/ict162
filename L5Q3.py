from tkinter import *
from bank import *
import tkinter.scrolledtext as st

class BankApp(Frame):
    def __init__(self, bank): # accepts a Bank object
        Frame.__init__(self)
        self._bank = bank
        self.master.title ("ATM")
        self.master.geometry('640x480')
        self.create()
        self.layout()
        
    def create(self):
        '''create 3 labels, 3 entries, 4 buttons, 1 scrolledtext'''
        self._lbID = Label (self, text = 'ID: ')
        self._lbPIN = Label (self, text = 'PIN: ')
        self._lbAmt = Label (self, text = 'Amount: ')
        self._etyID = Entry (self, width = 10)
        self._etyPIN = Entry (self, width = 10)
        self._etyAmt = Entry (self, width = 10)
        self._btnLog = Button (self, text = 'Login', command = self.login)
        self._btnDep = Button (self, text = 'Deposit', command = self.deposit)
        self._btnWD = Button (self, text = 'Withdraw', command = self.withdraw)
        self._btnCheck = Button (self, text = 'Check', command = self.check)
        self._stText = st.ScrolledText (self, width = 20, height = 15)
        
        # disable components
        self._etyAmt.configure(state = 'disabled')
        self._btnDep.configure(state = 'disabled')
        self._btnWD.configure(state = 'disabled')
        self._btnCheck.configure(state = 'disabled')
        
    def login(self):
        aID = self._etyID.get()
        pin = self._etyPIN.get()
        self._selectedAcc = self._bank.search(aID)
        if self._selectedAcc is None:
            txt = 'No such account ID'
        elif pin == self._selectedAcc.pin:
            txt = 'Login successful'
            # enable buttons and amount entry
            self._btnDep.configure(state = 'normal')
            self._btnWD.configure(state = 'normal')
            self._btnCheck.configure(state = 'normal')
            self._etyAmt.configure(state = 'normal')
        else:
            txt = 'Cannot login'
        self._stText.insert(END, txt + '\n')
        
    def check(self):
        if self._selectedAcc is not None:
            txt = f'Balance is ${self._selectedAcc.balance:.2f}'
            self._stText.insert(END, txt + '\n')
        
    def deposit(self):
        amt = float (self._etyAmt.get())
        if self._selectedAcc is not None:
            self._selectedAcc.deposit (amt)
            txt = f'${amt:.2f} deposited'
            self._stText.insert(END, txt + '\n')
        self._etyAmt.delete(0, END)
        
    def withdraw(self):
        if self._selectedAcc is not None:
            amt = float (self._etyAmt.get())
            if self._selectedAcc.withdraw(amt):
                txt = f'${amt:.2f} withdrawn'
            else:
                txt = 'Cannot withdraw'
            self._stText.insert(END, txt + '\n')
            
    def layout(self):
        '''place the components using grid'''
        self._lbID.grid(row = 0, column = 0)
        self._etyID.grid(row = 0, column = 1)
        self._lbPIN.grid(row = 1, column = 0)
        self._etyPIN.grid(row = 1, column = 1)
        self._btnLog.grid(row = 1, column = 2)
        self._lbAmt.grid(row = 2, column = 0)
        self._etyAmt.grid(row = 2, column = 1)
        self._btnDep.grid(row = 3, column = 0)
        self._btnWD.grid(row = 3, column = 1)
        self._btnCheck.grid(row = 3, column = 2)
        self._stText.grid(row = 4, column = 0, columnspan = 3)
        self.pack()
        
def main():
    bk = Bank('MyBank')
    ba1 = BankAccount ('A111', '123', 100)
    ba2 = BankAccount ('A222', '678', 200)
    ba3 = BankAccount ('A333', '345', 300)
    bk.add(ba1)
    bk.add(ba2)
    bk.add(ba3)
    
    app = BankApp(bk)
    app.mainloop()
    
main()