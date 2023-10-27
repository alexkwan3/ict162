from tkinter import *

class Q2(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title('BMI Demo App')
        self.master.geometry("300x200")
        
        self.create()
        self.layout()
        
    def create(self):
        '''radio buttons is a group of related buttons, only one is selected at any one time
        use a common variable to group radio buttons'''
        
        self._unit = StringVar()
        self._rb1 = Radiobutton (self, text = 'kg/m', variable = self._unit, value= 'kg')
        self._rb2 = Radiobutton (self, text = 'lb/in', variable = self._unit, value = 'lb')
        self._unit.set('kg') # set default selection
        self._lbWeight = Label (self, text = "Weight: ")
        self._lbHeight = Label (self, text = "Height: ")
        self._lbStatus = Label (self, text = 'status')
        self._etyWeight = Entry (self, width = 10)
        self._etyHeight = Entry (self, width = 10)
        self._btn = Button (self, text = 'BMI', command = self.calcBMI)
        
    def layout (self):
        self._rb1.grid (row = 0, column = 0)
        self._rb2.grid (row = 0, column = 1)
        self._lbWeight.grid (row = 1, column = 0)
        self._etyWeight.grid(row = 1, column = 1)
        self._lbHeight.grid (row = 2, column = 0)
        self._etyHeight.grid (row = 2, column = 1)
        self._btn.grid(row = 3, column = 0, columnspan=2)
        self._lbStatus.grid(row=4, column=0, columnspan = 2)
        
        self.pack() # will place in center of window
    
    def calcBMI(self):
        wt = float (self._etyWeight.get())
        ht = float (self._etyHeight.get())
        bmi = wt/(ht**2)
        if self._unit.get() == 'lb':
            bmi = bmi * 703
        self._lbStatus.configure(text = f'Height: {ht:.2f} Weight: {wt:.2f} BMI: {bmi:.2f}')
        self._etyWeight.delete(0, END) # clear text entry, can also use this for scrolledtext entry
        self._etyHeight.delete(0, END)
        
def q2():
    app = Q2()
    app.mainloop()
q2()