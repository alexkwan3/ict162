from tkinter import *
import random
import tkinter.scrolledtext as st # st is an alias for tkinter.scrolledtext

class Q1(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("HiLo Guessing Game")
        self.master.geometry('400x200')
        
        self._secret = random.randint(1,100)
        self.create()
        self.layout()
        
    def create (self):
        self._lbGuess = Label (self,text='Guess')
        self._etyGuess = Entry (self, width = 10)
        self._btn = Button (self, text = 'Guess', command=self.checkGuess)
        # self._lbStatus = Label (self, text='Status')
        self._stTxt = st.ScrolledText(self, width = 20, height = 5)
        
    def layout(self):
        self._lbGuess.grid(row=0, column=0)
        self._etyGuess.grid(row=0,column=1)
        self._btn.grid(row=1, column=0,columnspan=2)
        # self._lbStatus.grid(row=2,column=0,columnspan=2)
        self._stTxt.grid(row = 2, column = 0, columnspan=2)
        self.grid()
        
    def checkGuess(self):
        guess = int(self._etyGuess.get())
        if guess == self._secret:
            txt = f'{guess} correct'
            # to disable the button
            self._btn.configure(state='disabled') # to enable use 'normal'
        elif guess < self._secret:
            txt = f'{guess} too low'
        else:
            txt = f'{guess} too high'
        # self._lbStatus.configure(text=txt)
        self._stTxt.insert(END, txt + '\n') # END is a constant that marks the last column in scrolledText
        
def q1():
    app = Q1()
    app.mainloop()
q1()