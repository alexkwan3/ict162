from datetime import *

class Guest:
    '''models a hotel guest
    it has 3 attributes: passport (str), name (str), country (str)
    it has property methods for passport, name, and country
    it has accessor method isBlacklisted()
    it has mutator method blacklist()
    it has __str__() method'''
    
    def __init__(self, passport, name, country):
        self._passport = passport
        self._name = name
        self._country = country
        self._blacklistedReason = []
        
    @property
    def passport (self): return self._passport
    @property
    def name (self): return self._name
    @property
    def country (self): return self._country
    
    def blacklist (self, dateReported, reason):
        self._blacklistedReason.append([dateReported, reason])
        
    def isBlacklisted(self):
        if self._blacklistedReason == []:
            return False
        else:
            return True
        
    def __str__(self):
        BL = self.isBlacklisted()
        if BL is False:
            return f'Passport number: {self._passport}\nName: {self._name}\nCountry: {self._country}'
        else:
            txt = '<< Blacklisted on date, reason >>\n'
            for n in self._blacklistedReason:
                txt += f'> {n[0]:%d-%b-%Y}\t{n[1]}\n'
            return f'Passport number: {self._passport}\nName: {self._name}\nCountry: {self._country}\n{txt}'