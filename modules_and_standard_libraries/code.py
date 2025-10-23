# import my_module
from my_module import fetchIndexNumber, test
import sys
import random
courses = ['maths','english', 'urdu', 'science']
# index = my_module.fetchIndexNumber(courses, 'english')
index = fetchIndexNumber(courses, 'urdu')
# print(index)
# print(test)

print(sys.path)

randomCourse = random.choice(courses)
print(randomCourse)
randomCourse = random.choice(courses)
print(randomCourse)
randomCourse = random.choice(courses)
print(randomCourse)


import math

rad = math.radians(90)
print(rad)
print(math.sin(rad))
print(math.cos(rad))

import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2023)) 


import os
print(os.getcwd())
print(os.getcwdb())
print(os.__file__)