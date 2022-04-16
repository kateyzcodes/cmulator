# from pathfinder import *
from campus import *
# from relationship import *
# from shops import *
# from utilityf import *
import random

class Grade(object):
    def __init__(self, course):
        self.course = course
        self.score = 100.0
    
    def factorGrade(self, course, assignment):
        gradeGiven = assignment.gradeIt()
        if assignment.type not in course.grades:
            course.grades[assignment.type] = [gradeGiven]
        else:
            course.grades[assignment.type].append(gradeGiven)

class Assignment(object):
    def __init__(self, type, perf):
        self.type = type
        self.perf = perf
    
    def gradeIt(self):
        if self.perf == True:
            return (random.randrange(80, 101))
        elif self.perf == None:
            return (random.randrange(60, 80))
        elif self.perf == False:
            return (random.randrange(0, 60))