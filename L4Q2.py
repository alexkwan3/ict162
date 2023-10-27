class InvalidAssessmentException(Exception):
    '''subclass of Exception
    use when error excountered using Assessment / TutorialGroup object'''
    
class Assessment:
    '''models an assessment
    it has a class attribute: max marks
    it has attributes: id (str) and mark (float)
    it has property methods for id and mark
    it has setter method for mark
    it has class method: getMaxMarks() and setMaxMarks()
    it has __str__() method'''
    
    _max = 100 # class variable
    
    def __init__(self, id, mark):
        if mark <= self._max:
            self._id = id
            self._mark = mark
        else:
            raise InvalidAssessmentException (f'Error! Mark cannot exceed {Assessment._max}')
        
    @property
    def id(self):
        return self._id
    @property
    def mark(self):
        return self._mark
    
    @mark.setter
    def mark(self,newMark):
        if 0 <= newMark <= self._max:
            self._mark = newMark
        else:
            raise InvalidAssessmentException (f'Error! Mark must be between 0-{Assessment._max}.')
        
    @classmethod
    def getMaxMarks(cls):
        return cls._max
    @classmethod
    def setMaxMarks(cls, newMax):
        cls._max = newMax
        
    def __str__(self):
        return f'ID: {self._id} Mark: {self._mark}'
    
class TutorialGroup:
    '''models a tutorial group
    it has 2 attributes: name (str) and dictionary (key is id, value is mark)
    it has mutator methods: add(), remove(), adjust()
    it has __str__() method'''
    
    def __init__(self, name):
        self._name = name
        self._assessment = {} # empty dictionary
    
    '''may raise InvalidAssessmentException when id already exists'''
    
    def add(self, id, mark):
        if id in self._assessment.keys():
            raise InvalidAssessmentException (f'Assessment for {id} already added!')
        else:
            self._assessment[id] = mark
            # self._assessment[id] = Assessment (id,mark) # value is Assessment object
            
    '''may raise InvalidAssessmentException when id not found or mark != 0'''
    
    def remove(self, id):
        if id not in self._assessment.keys():
            raise InvalidAssessmentException (f'Assessment for {id} not found!')
        elif self._assessment[id] != 0:
            raise InvalidAssessmentException (f'Cannot remove if assessment mark is not 0')
        else:
            self._assessment.pop(id)
            
    '''may raise InvalidAssessmentException when id is not found or when newMark is the same as mark'''
            
    def adjust(self, id, newMark):
        if id not in self._assessment.keys():
            raise InvalidAssessmentException (f'Error: {id} not found!')
        elif newMark == self._assessment[id]:
            raise InvalidAssessmentException (f'Error: {newMark} is the same as existing {self._assessment[id]}')
        else:
            # self._assessment[id] = Assessment(id, newMark)
            self._assessment[id] = newMark
    
    def __str__(self):
        # returns a single string containing all assessment objects' str
        txt = f'Tutorial Group: {self._name}\n'
        for a, b in (self._assessment.items()):
            txt += f'{a}:{b}\n'
        return txt
    
def menu():
    print ('1. Add assessment')
    print ('2. Remove assessment')
    print ('3. Adjust assessment')
    print ('4. List all assessments')
    print ('5. Quit')
    opt = int (input("Enter option: "))
    return opt
            
def q2():
    a = Assessment('pcq1', 13)
    print (a)
    try:
        a.mark = 100
        print (a)
    except InvalidAssessmentException as e:
        print (e)
    tg = TutorialGroup('T08')
    try:
        tg.add('pcq1', 23)
        tg.add('pcq2', 50)
        # tg.add('pcq1', 33)
        # tg.remove('pcq1')
        tg.adjust('pcq1', 0)
        print (tg)
    except InvalidAssessmentException as e:
        print (e)
        
    while True:
        try:
            opt = menu()
            if opt == 5:
                break
            elif opt == 1:
                aID = input ("Enter ID: ")
                mark = int (input("Enter mark: "))
                tg.add(aID, mark)
            elif opt == 2:
                aID = input ("Enter ID: ")
                tg.remove(aID)
            elif opt == 3:
                aID = input ("Enter ID: ")
                newMark = int (input ("Enter new mark: "))
                tg.adjust(aID, newMark)
            elif opt == 4:
                print (tg)
        except InvalidAssessmentException as e:
            print (e)
    print ("End of program")
q2()

def test():
    b = Assessment ('pcq1', 20)
    print (b)
    tg = TutorialGroup('T08')
    tg.add(b._id, b._mark)
    print (tg)
# test()