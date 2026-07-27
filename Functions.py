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
'''
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