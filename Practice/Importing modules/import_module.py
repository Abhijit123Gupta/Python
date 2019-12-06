# import my_module   =imports the my_module file :executes all the print statements
#from my_module import test_str  	=imports specific things from my_module   
#print(test_str)


#import my_module as module   #my_module can be replaced by module
#courses = ['math', 'english', 'hindi', 'Physics', 'Comp_Science']

#index = module.find_index(courses, 'Comp_Science')
#print(index)


#from my_module import *   :imports everything   


from my_module import test_str, find_index   #my_module can be replaced by module
courses = ['math', 'english', 'hindi', 'Physics', 'Comp_Science']

index = find_index(courses, 'Comp_Science')
print(index)
print(test_str)

#import sys
#print(sys.path)  #directories where python looks for modules for importing

import math
rads = math.radians(90) 
print(rads)
print(math.sin(rads))



import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))


import os
print(os.getcwd())
print(os.__file__)
