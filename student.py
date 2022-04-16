from utilityf import *
from campus import *
from inventory import *
from wallet import *

class Student(object):
    def __init__(self, firstName, lastName, major):
        # personal info
        self.firstName = firstName
        self.lastName = lastName
        self.andrewID = firstName + lastName[0]
        self.andrewID = self.andrewID.lower()
        # bars
        self.health = Bar('health')
        self.happiness = Bar('happiness')
        self.energy = Bar('energy')
        # actions
        self.sleep = Action('sleep', (20, 30, 15), self.getBars())
        self.eat = Action('eat', (30, 25, 20), self.getBars())
        self.workout = Action('workout', (25, -20, 25), self.getBars())
        self.attendLecture = Action('attendLecture', (0, -20, -15), self.getBars())
        # academic info
        self.qpa = 4.0
        self.courses = determineCourses(major)
        self.schedule = determineSchedule(self.courses)
        # extra features
        self.inventory = Inventory(self)
        self.wallet = Wallet(self, True)

    def statsCap(self):
        if self.health.level < 0:
            self.health.level = 0
        if self.health.level > 100:
            self.health.level = 100
        if self.energy.level < 0:
            self.energy.level = 0
        if self.energy.level > 100:
            self.energy.level = 100
        if self.happiness.level < 0:
            self.happiness.level = 0
        if self.happiness.level > 100:
            self.happiness.level = 100

    def eating(self, item):
        if self.inventory.use(item) == True:
            self.health.level += item.healthEffect
            self.energy.level += item.energyEffect
            self.happiness.level += item.happyEffect
            self.statsCap()
        else:
            return False

    def sleeping(self, duration):
        if duration == 'nap':
            self.health.level += 10
            self.energy.level += 15
            self.happiness.level += 10
            self.statsCap()
        elif duration == 'sleep':
            self.health.level += 20
            self.energy.level += 30
            self.happiness.level += 20
            self.statsCap()
        else:
            return False

    def workingOut(self, duration):
        if duration == 'short':
            self.health.level += 15
            self.energy.level -= 15
            self.happiness.level += 15
            self.statsCap()
        elif duration == 'long':
            self.health.level += 25
            self.energy.level -= 30
            self.happiness.level += 25
            self.statsCap()
        else:
            return False

    def attendingSchool(self, course, event):
        if event == 'lecture':
            self.energy.level -= 30
            self.happiness.level -= 15
            self.statsCap()
            LecturePart = Assignment('part', True)
        elif event == 'OH':
            self.energy.level -= 15
            self.happiness.level -= 10
            self.statsCap()
            OHPart = Assignment('part', True)

    def getBars(self):
        return [self.health, self.energy, self.happiness]

    def getActions(self):
        return [self.sleep, self.eat, self.workout, self.attendLecture]

    def calcQPA(self):
        totalAvg = 0
        for course in self.courses:
            totalAvg += course.average
        result = str((totalAvg/(len(self.courses)))/25)
        result = result[:-2]
        return result

def determineCourses(major):
    return major.courses

def determineSchedule(courses):
    schedule = dict()
    for day in range(0, 7):
        if day == 5 or day == 6:
            if day not in schedule:
                schedule[day] = None
        elif day % 2 == 0:
            if day not in schedule:
                schedule[day] = [courses[0], courses[2]]
        elif day % 2 == 1:
            if day not in schedule:
                schedule[day] = [courses[1]]
    return schedule

def getNextBestStep(student):
    utilities = dict()
    actions = student.getActions()
    for action in actions:
        # add backtracking style check here for how stats bars will 
        # look after a potential action is performed
        action.utility = getUtility(action)
        utilities[action.name] = action.utility
    bestU = -1.0
    for actionU in utilities:
        print(f'{actionU} = {utilities[actionU]}')
        if bestU < utilities[actionU]:
            bestU = utilities[actionU]
        print('----------')
    for action in utilities:
        if utilities[action] == bestU:
            return action
