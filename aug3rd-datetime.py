'''
datetime --> date,time module functionalities
This module includes
various classes and methods to handle date and time operations efficiently.'''
import datetime
#print(dir(datetime))
from datetime import datetime
a = datetime.now() #returns current timestamp
print(a)
print(type(a))
#based on above datetime object we can extract separately as below
d = datetime.now()
print(d.date())
da = d.day
m = d.month
y = d.year
print(f'Today is {da}-{m}-{y}')
g = datetime.today()
print(g)
print(type(g))
h = g.weekday() #Monday - 0
print(h)
k = g.isoweekday() #ISO --> 0- Sunday
print(k)
l = g.time()
print(l)
#StringFormatting  -->convert datetime to string
print(g.strftime('%W')) #number of days in this month
print(g.strftime("%m")) 
print(g.strftime("%w"))
print(f'Today is {g.strftime("%A")}')