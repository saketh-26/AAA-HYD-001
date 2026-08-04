'''
datetime --> date,time module functionalities
This module includes
various classes and methods to handle date and time operations efficiently.'''
import datetime
#print(dir(datetime))
from datetime import datetime
'''a = datetime.now() #returns current timestamp
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

#We can create a datetime object 
b = datetime(2026,8,15)
print(b)
print(type(b))
c = datetime(day=16,month=9,year=2026,hour=10,minute=30)
print(c)
print(type(c))
print(dir(datetime))

#Accept input from user -->convert to datetime object --> return the 
#string format (part day,month name)
from datetime import datetime
d,m,y = map(int,input("Enter the values").split(','))
print(d,m,y)
d_obj = datetime(y,m,d)
print(d_obj)
print(f'Today is {d_obj.strftime("%A")}') #%A --> full name of day of week
print(f'The month is {d_obj.strftime("%B")}') #%B -->full mnth name
'''

#strptime() -->Stringpointoftime --->datetime --> str format
#timedelta --> handling time difference
from datetime import datetime,timedelta
f = datetime.now()
#print(f)
#print(type(f))
d_obj = datetime.strptime("26-12-1993","%d-%m-%Y")
#print(d_obj)
#print(d_obj.strftime('That day was %A'))
print(f)
print(d_obj)

#days,hours,minutes,secods
diff = timedelta(days=5,hours=10)
print(diff)

print(f-diff)
print(f + timedelta(hours=5,minutes=30)) #this returns current IST timezone
d = f+timedelta(hours=5,minutes=30)
print(d)
print(f'Future date is {d+timedelta(days=5,hours=10)}')

#time --> time functionalities
import time
print(dir(time))
print(time.tzname)
print(time.ctime()) #returns in string
d_obj = time.localtime() #returns in structure
y = d_obj.tm_year
month = d_obj.tm_mon
day = d_obj.tm_mday
print(f"Date is {day}-{month}-{y}")