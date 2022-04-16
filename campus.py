from grades import *
from relationship import *

class startingPoint(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Building(object):
    def __init__(self, name, subjects, entrance):
        self.name = name
        self.subjects = subjects
        self.entranceRow = entrance[0]
        self.entranceCol = entrance[1]

class Subject(object):
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses

class Course(object):
    def __init__(self, name, professor, ta):
        self.name = name
        self.professor = professor
        self.ta = ta
        self.grades = dict()
        self.average = self.calcAvg()
    
    def calcAvg(self):
        hwAvg = 0
        testAvg = 0
        partAvg = 0
        for gradeType in self.grades:
            if gradeType == 'hw':
                for score in self.grades[gradeType]:
                    hwAvg += score
                hwAvg /= len(self.grades[gradeType])
            elif gradeType == 'test':
                for score in self.grades[gradeType]:
                    testAvg += score
                testAvg /= len(self.grades[gradeType])
            elif gradeType == 'part':
                for score in self.grades[gradeType]:
                    partAvg += score
                partAvg /= len(self.grades[gradeType])
        return ((hwAvg*0.4) + (testAvg*0.3) + (partAvg*0.3))*4

campusStart = startingPoint(23, 25)

# COURSES
# Business
Economics = Course('Economics', BizProf1, [])
Management = Course('Management', BizProf2, [])
Accounting = Course('Accounting', BizProf3, [])

# Art
Sketching = Course('Sketching', ArtProf1, [])
Painting = Course('Painting', ArtProf2, [])
ArtTheory = Course('Art Theory', ArtProf3, [])

# Math
Calculus = Course('Calculus', MathProf1, [])
NumberTheory = Course('Number Theory', MathProf2, [])
Algebra = Course('Algebra', MathProf3, [])

# Science
Biology = Course('Biology', SciProf1, [])
Chemistry = Course('Organic Chemistry', SciProf2, [])
Physics = Course('Physics', SciProf3, [])

# English
Poetry = Course('Intro to Poetry', EngProf1, [])
Grammar = Course('Grammar 101', EngProf2, [])
Essay = Course('Essay Writing', EngProf3, [])

# History
Feminism = Course('History of Feminism', HistProf1, [])
ChineseHist = Course('Chinese Dynasties History', HistProf2, [])
ArtHist = Course('Art History', HistProf3, [])

# Computer Science
CSFundProg = Course('15-112', CSProf1, [Lauren, Melinda])
AlgoTheory = Course('Algorithm Theory', CSProf2, [])
DataSecurity = Course('Data Security', CSProf3, [])


# SUBJECTS
Business = Subject('Business', [Economics, Management, Accounting])
Art = Subject('Art', [Sketching, Painting, Accounting])
Math = Subject('Math', [Calculus, NumberTheory, Algebra])
Science = Subject('Science', [Biology, Chemistry, Physics])
English = Subject('English', [Poetry, Grammar, Essay])
History = Subject('History', [Feminism, ChineseHist, ArtHist])
CompSci = Subject('Computer Science', [CSFundProg, AlgoTheory, DataSecurity])

Buildings = []

# BUILDINGS
UniC = Building('University Center', None, (11, 18))
Buildings.append(UniC)
Wean = Building('Wean Hall', [English, History], (13, 37))
Buildings.append(Wean)
Doherty = Building('Doherty Hall', [Math, Science], (29, 9))
Buildings.append(Doherty)
Tepper = Building('Tepper Building', [Business], (31, 25))
Buildings.append(Tepper)
Hunt = Building('Hunt Library', None, (2, 18))
Buildings.append(Hunt)
CFArt = Building('College of Fine Arts', [Art], (11, 2))
Buildings.append(CFArt)
Gates = Building('Gates Center For Computer Science', [CompSci], (23, 17))
Buildings.append(Gates)


