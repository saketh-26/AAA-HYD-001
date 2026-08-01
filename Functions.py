'''
POP --> Procedure Oriented Programming --> Functions
Function --> A Function is a block of code (statements) which performs a specific task
It is a resuable code -->readbility,reusability and easy to maintain
User defined Functions --> def 
Built-in Functions -->Python by default
Anonymous Functions --> lambda (map,filter,reduce)
Recursive Functions -->Factorial,Fibonacci -->Decorators

Syntax  -->User defined Functions
def fname(parameters): #function header 
    """Doc String (Description of Function)"""
    statement(s)......              Body of Function
    return value(s).... 
fname(arguments) #function call

#Sample Function to understand its importance...

def add(a,b): 
    """Sample Add Function"""
    c = a + b 
    #print(f'Value of c is {c}')
    return c
#add(12,3)
#add(12,3.5)
#add('code','gnan')
print(add([12,3,45],[4,3,5]))
print(add('code','gnan'))
#Assigning Function to a variable
result = add('Code','gnan')
print(result)

#Parameters --> Below categories
#Positional Arguments --> count of arguments to be matched
#Default arguemnts ->we can make argument as default
#Keyword arguemnts -->order/keyword name to be matched
#Variable Length arguments (*args) -->we can pass any number of positional arguments can be given
#Keyword Variable length arguments (**kwargs) -->we can pass any number of keyword arguemnts 

#Grocery Purchase 
def grocery(item,price):
#def grocery(item,price=40):
#def grocery(item="Jam",price):#nondefault always follows default
#def grocery(item="Jam",price=45):
    """Usage of Positional,Default and Keyword Arguments"""
    print(f'Item is {item}')
    print(f'Value of Item is {price}')
#grocery('Milk',30)
#grocery('Bread')#typerror as count is mismatch
#grocery()
grocery(price=45,item="Milk")
#grocery(price=45,Item="Milk") #TypeError -->keyword item is mismatching 

#Variable length arguments -->We can define any number of positional arguments
#Python stores in tuple format,we use * notation to define variable lengthj arguments

def sample(*args) : 
    """Usage of Variable length arguments"""
    print(args) 
    print(type(args))
sample()
sample(1,2,3)
sample(1,23.5,'codegnan',23+5j)
#sample(name="saketh") #TypeError 

#To return the sum of given values....

def add(*a):
    """Summation of given objects"""
    result = 0 #output object
    #print(a)
    for i in a:
        #print(i)
        if type(i) in (int,float):
            result = result + i
    return result
#add() 
#print(add(1,3))
print(add(1,4,'codegnan',2.3,34,2.5,2+4j))

#Keyword Variable length arguments --> Any number of keyword arguments can be passed to function
#Data is stored in dictionary --> we use ** notation

def sample(**kwargs):
    """Usage of Keyword Variable length arguments"""
    print(kwargs) 
    print(type(kwargs))
sample()
sample(name = "abhi",age=20,course = "AAI")

def grocery(**items):
    """Groceries List"""
    print(items)
    #for i in items:
        #print(i) #it returns each key
    #for i in items.values():
        #print(i)
    for key,value in items.items():
        print(f'Key is {key}')
        print(f'Value is {value}')
grocery()
grocery(name='Milk',price=35,quantity='1000ml',brand="Heritage")


#Converting BMI Usecase to Function

def bmi_calc(**kwargs):
    """BMI Usecase"""
    while True: 
        try: 
            weight = int(input("Enter the weight in kgs.."))
            height = float(input("Enter the height in metres.."))
            if weight > 0 and height > 0:
                break
            else:
                print(f'Make sure to enter only +ve values,no Negative values..')
        except ValueError:
            print('Invalid input only integer for weight/int,float for height,enter properly')
    bmi = (weight) / ((height)**2)
    if bmi <18.5 :
        print(f'You are Underweight as BMI is {bmi}')
    elif 18.5<=bmi<24.9:
        print(f'You are in Perfect shape,BMi is {bmi}')
    elif 25<=bmi<29.9:
        print(f'You are Overweight need to maintain diet,BMI is {bmi}')
    elif bmi>=30:
            print(f'Obesity,your BMI is {bmi}')
bmi_calc()

def bmi_calc(*kwargs):
    """BMI Usecase"""
    while True: 
        try: 
            weight = int(input("Enter the weight:"))
            height = float(input("Enter the height in meters:"))
            if weight > 0 and height > 0:
                break
            else:
                print(f'Make sure to enter only +ve values,no Negative values..')
        except ValueError:
            print('Invalid input only integer for weight/int,float for height,enter properly')
    bmi = (weight) / ((height)**2)
    if bmi <18.5 :
        print(f'You are Underweight as BMI is {bmi}')
    elif 18.5<=bmi<24.9:
        print(f'You are in Perfect shape,BMi is {bmi}')
    elif 25<=bmi<29.9:
        print(f'You are Overweight need to maintain diet,BMI is {bmi}')
    elif bmi>=30:
            print(f'Obesity,your BMI is {bmi}')
bmi_calc()

#BMI Usecase -->Unit Converter -->Function (*args / **kwargs) -->Home task

#Scope of Variables --> Scope --> the field (place) where we are accessing the variables

-->Local Variables
-->Global Variables
-->Global keyword usage
-->Enclosing variables (nonlocal keyword)

#Local variables --> Variables defined inside the function

def fname():
    """Usage of local variables"""
    name = "Codegnan" #local variable
    return name
print(fname())
#print(name) #NameError

#Global variable --> it is defined and accessible in the entire module (entire Python script)

name = "Codegnan"
def uname():
    """Glocal Scope"""
    return name
print(uname())
print(f'Company name is {name}')
print(name + 'AAI')

name = "Codegnan"
def uname():
    """Glocal Scope"""
    name = "Saketh"
    return name
print(uname())
print(f'Company name is {name}')
print(name + 'AAI')

#global keyword -->we want to modify global scope variable and use in function and update 
#accordingly

count = 15
def update():
    """Usage of global keyword"""
    global count
    count = count + 10
    return count
print(update())
print(f'Updated Value of count is {count}')

#Enclosing Scope -->non local keyword --> Nested Functions 
def outer():
    """Outer Function"""
    count = 10
    def inner():
        nonlocal count
        count = count + 5
        return count
    print(inner())
    return count
print(outer())

#LEGB --> Local Scope,Enclosing Scope,Global,Built-ins 
#Built-in Scope -->builtin functions can be used as variables but it overrides its behaviour
#(should be avoided)
len = 34
print(len)
#print(len('codegnan')) #here its overrridden
'''

#Pass by Value 
#Pass by Object reference

#Pass by Value Reference --> Immutable objects (int,float,str,tuple,frozenset)
'''
def update(number):
    """Pass by Value Reference works"""
    number = 15
    number = number * 5
    return number
print(update(5))
number = 23
print(update(number))
print(number)
print(update('3'))

def update(number):
    """Example Usage"""
    return number *3
print(update(3))
print(update(25))
number = 45
print(update(number))

#Pass by Object Reference --> Mutable Objects (list,set,dict)

def update(items):
    """Pass by Object Reference"""
    items.append("Mobile")
    return items
cart = ['Laptop','Charger']
print(update(cart))
print(cart)

#Functions are termed as First Class Objects -->
#A function inside another function -->Enclosing Scope (nonlocal)
#A function can be used as an argument to another function -> list(map(int,input()))
#A function can call itself (Recursive Functions)
#A function can return another function

#Built-in functions --> Python by default has built-ins which makes the logic easier
if __name__ == "__main__":
    #print(2+34)
    #print(dir())
    print(dir(__builtins__)) #list of all built-ins (Errors and Functions)
#We will discuss some of widely used Built-in Functions
print(abs(-23)) #returns the absolute value (+ve)
#all(),any() -->checks for the values in a iterable -->Boolean
data = ['saketh','sai','akash']
print(all(data))
data.clear()
print(all(data))
d = [None,23,45]
print(all(d))
print(any(d))
print(bin(6)) #returns binary reprsentation of an object
print(chr(65)) #input any integer -> returns specific character
print(bool(0)) #output Boolean (True / False)
print(complex()) #returns complex number
print(dict(name = "saketh",place = "codegnan")) #returns a dictionary

print(divmod(5,3)) #returns the division modulus in a tuple..
#enumerate () , eval()

details = ['codegnan','saketh','AAI']
print(dict(enumerate(details))) #default counter objct is 0
print(dict(enumerate(details,1)))
#O/p :

0 : 'Codegnan'
1 : 'Saketh'
2 : 'AAI'

for i in details:
    print(details.index(i),':',i)

a = eval(input("Enter a dictionary:"))
print(a)
print(id(a))
b = (23,1,4,6)
print(tuple(sorted(b))) #sorted () by default returns List
print(min(b))
print(max(b))
print(max(['C','code','Data']))
print(pow(2,3))
print(tuple(reversed(b)))
print(round(4.56))
print(round(4.567,2))
details = ['codegnan','AAAI']
ages = [7,1]
d = dict(zip(details,ages)) #zip-->combines multiple collections into one iterable (list,dict)
print(d)


#Recursive Functions,Anonymous Functions 
#Recursive Functions --> A function calling itself,where it makes the smaller problem is broken into multiple times
#Depends on two cases --> Base Case (it indicates when to stop the recursion)
#                     ---> Recursive case (it makes the problem to be repeated)

Syntax:

def function() :
    if base_condtion:
        return
    function() #we write our recursive
function()

def test():
    """Without Base case"""
    return test()
print(test())

#5! --> 5 * (5-1) * (5-2) * (5-3) * (5-4) -->120

#Factorial approach using Recursion 

def factorial(n):
    """Recursive approach"""
    if n == 0 or n == 1:
        return 1
    elif n <0 :
        return "No -ve values only +ve values to be accepted"
    else:
        return n * factorial(n-1)
n = int(input("Enter a value:"))
print(factorial(n))

#Find the sum of natural numbers till 10 using Recursive Function
#Just in above case change the logic as n + funname(n-1)

#Task : Build a simple choice chooser 
#1 --> Recursion logic for Factorial 
#2 --> Sum of numbers (Recursion)
#3 --> BMI calculate
#4 --> Fibonacci series 
#5 --> ATM Usecase 

#Anonymous Functions --> Nameless Functions,we define them by using lambda keyword
#filter(),map() 

#Create a function to return the area of rectangle
def rectangle(l,b):
    """Sample function to get area of rectangle"""
    return l*b
print(rectangle(5,4))
b = rectangle(4,5)
print(b)

#Syntax: --> var_name = lambda parameters : expression
b = lambda l,b : l*b
print(type(b))
print(b(5,6))

#Find the area of square using lambda
c = lambda side : side * side
side = int((input("Enter the measurements:")))
print(c(side))
'''
#User Registration in a webpage --> name 
#First Name --> input
#Last Name --> input
#Full Name

#Write user defined them anonymous function
#firstname = input("Enter the first name:").lower()
#lastname = input("Enter the last name:").lower()
'''def full_name(firstname,lastname):
    """ Normal Function Usage """
    return firstname.title() + " " + lastname.title()
print(full_name(firstname,lastname))

#Same using anonymous 
full_name = lambda firstname,lastname : firstname.title() + " " + lastname.title()
print(full_name(firstname,lastname))

#To get even number from user input
n = int(input("Enter a value:"))
result = lambda n : n if n%2 == 0 else "Odd"
print(result(n))

#length of sequences
name = input("Enter the message:")
result = lambda name : len(name)
print(result(name))

#filter(),map() 

#filter(function,iterable) --> returns the filtered values by satisfying the condition
#yielding the value from iterable

#List of integers
a = list(map(int,input("Enter the values:").split(',')))
print(a)
#Filter only even numbers
b = list(filter(lambda x:x%2==0,a))
print(b)

names = ['Pavan','Abhiram','Nihanth','Saikiran','Roshan','Vasanthi','Manimala']
#return names whose length > 6
final_names = list(filter(lambda name:len(name)>6,names))
print(final_names)

#map() --> it will apply for every value from multiple iterables
a = list(map(int,input("Enter the values:").split(',')))
print(a)

names = ['codegnan','saketh','agenticai']
result = list(map(lambda name:name.upper(),names))
print(result)

prices = [1000,2500,3500,4000]
final_price = list(map(lambda price : (price - price * 0.1),prices))
print(final_price)
'''
#reduce() --> this makes complete iterable to be a single value -->functools
from functools import reduce
numbers = [1,4,5,7,8] #sum of numbers 
result = reduce(lambda a,b:a+b,numbers)
print(result)
prod = reduce(lambda a,b:a*b,numbers)
print(prod)


