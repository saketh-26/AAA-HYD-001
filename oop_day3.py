'''
OOP -->Encapsulation,Inheritance

#Encapsulation --> It is also one of the key feature of OOP.It actually bundles
the attributes (data) and methods (functions) into a whole single unit (class)
it helps to main data integrity,privacy,code maintainability,security..

Type of Attributes using Encapsulation:
Public -->can be accessible anywhere inside and outside the class
Protected -->we wanted to make it for internal use,can be accessible outside the
class
Private -->hidden,cannot accessible directly
For usage of Protected along with Private attributes we use underscore notation


#Usage of Public Attributes

class Users:
    """Usage of Public Attributes"""
    def __init__(self,name):
        self.name = name  #Public Attribute

    def display(self):
        return f'{self.name} is in AAA batch'

user1 = Users("saketh kallepu")
print(user1.__dict__)
print(user1.display())
user1 = Users("Saketh")
print(user1.display())
print(user1.__dict__)

class Users:
    """Usage of Protected Attributes"""
    def __init__(self,name,_otp):
        self.name = name  #Public Attribute
        self._otp = _otp #Protected Attribute

    def display(self):
        print(f'{self.name} is in AAA batch')
        print(f'OTP is {self._otp}')

user1 = Users("Agent",23456)
print(user1._otp)
user1.display()
user1._otp = 34567
print(user1.__dict__)
user1.display()

class Users:
    """Usage of Public,Protected&Private Attributes"""
    def __init__(self,name,_otp,password):
        self.name = name  #Public Attribute
        self._otp = _otp #Protected Attribute
        self.__password = password #Private Attribute

    def display(self):
        print(f'{self.name} is in AAA batch')
        print(f'OTP is {self._otp}')
        print(f'Logged in with {self.__password}')
user1 = Users("saketh",23456,"admin123")
print(user1.name)
print(user1._otp)
#print(user1.password) #Attribute Error
print(dir(user1))
print(user1._Users__password) #NameMangling
user1.display()

#Accessing Private Attributes using getter and setter methods..

class Users:
    """Usage of Public,Protected&Private Attributes"""
    def __init__(self,name,password):
        self.name = name  #Public Attribute
        self.__password = password #Private Attribute

    #Accessing Private attribute using getter method
    def get_password(self):
        return "******"  #here we are accessing

    #Using Setter Method we want to have validations
    def set_password(self,new_password):
        if len(new_password) < 6:
            print(f'Error in validating the password,enter atleast 6 characters')
        else:
            self.__password = new_password
            print(f'The password is modified and it is {self.__password}')
user1 = Users("saketh","admin123")
print(user1.get_password())
print(user1.__dict__)
user1.set_password("123") #validation failed
user1.set_password("qwerty123") #validation pass
print(user1.__dict__)

#Create a scenario for Protected Attributes use getter() and setter()

class Users:
    """Usage of Public,Protected&Private Attributes"""
    def __init__(self,name,otp,password):
        self.name = name  #Public Attribute
        self._otp = otp #Protected Atttribute
        self.__password = password #Private Attribute

    #Accessing Protected attribute using getter method
    def get_otp(self):
        return self._otp  #here we are accessing

    #Using Setter Method we want to have validations
    def set_otp(self,new_otp):
        if len(new_otp) < 4:
            print(f'Error in validating the OTP')
        else:
            self._otp = new_otp
            print(f'day10.py_otp}')

    #Accessing Private attribute using getter method
    def get_password(self):
        return "******"  #here we are accessing

    #Using Setter Method we want to have validations
    def set_password(self,new_password):
        if len(new_password) < 6:
            print(f'Error in validating the password,enter atleast 6 characters')
        else:
            self.__password = new_password
            print(f'The password is modified and it is {self.__password}')
user1 =Users(name ="saketh",password ="admin123",otp='123456')
print(user1.__dict__)
print(user1.get_otp())
user1.set_otp('123')
user1.set_otp('3456789')
print(user1.get_otp())
print(user1.__dict__)
'''

#Inheritance -->One of the key principles in OOP,which mainly focuses on
#acquiring the properties from base class(parent class)
#to dervied class(child class)
'''
Syntax for Inheritance :
class Parent:
    statement(s)...
    ......
class Child(Parent):
    statement(s).....
    .......
'''
#Single Inheritance,Multiple Inheritance,Multilevel Inheritance,Hybrid Inheritance

#Scenario of Usernames creation and Updation in Profile page
'''
class Users:
    """User details"""
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def full_name(self):
        return self.fname + self.lname
#user1 = Users("saketh","kallepu")
#print(user1.full_name())
class Update_Users(Users):
    def update_name(self):
        return self.fname.title().strip()+" "+self.lname.title().strip()
user1 = Update_Users("saketh","kallepu")
print(user1.full_name())
print(user1.update_name())
'''

#Single Inheritance
'''
Users -->Parent

Update User1 (Users) -->child1

Update User2(Users) -->child2
'''

#Whatsapp scenario -->Users,Business Users (Single Inheritance)
































    
                  




















        



























