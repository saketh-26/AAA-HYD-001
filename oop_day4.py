'''
Inheritance -->Single Inheritance,Multiple Inheritance,Multilevel Inheritance 
#super() 

class Parent:
    pass
class Child(Parent):
    pass
class Child2(Parent):
    pass
'''
#Banking Scenario
'''
class RBI:
    """Parent Class with major cash holding"""
    available_cash = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        print(f'RBI has {cls.available_cash}')
class SBI(RBI):
    pass
class HDFC(RBI):
    hdfc_cash = 5000000 
    @classmethod
    def hd_cash(cls):
        print(f'HDFC Cash is {cls.hdfc_cash}')
        print(f'Total Cash accessible for HDFC is {cls.hdfc_cash + cls.available_cash}')
#a = RBI()
#print(a.available_cash)
#a.rbi_cash()
#sbi = SBI()
#print(dir(sbi))
#print(sbi.available_cash)
#sbi.rbi_cash()
hdfc = HDFC()
hdfc.hd_cash()

class RBI:
    """Parent Class with major cash holding"""
    cash = 10000000 #class attribute
    @classmethod
    def rbi_cash(cls):
        print(f'RBI has {RBI.cash}')
class SBI(RBI):
    pass
class HDFC(RBI):
    cash = 5000000 
    @classmethod
    def hd_cash(cls):
        print(f'HDFC Cash is {HDFC.cash}')
        print(f'Total Cash accessible for HDFC is {RBI.cash + HDFC.cash}')
hdfc = HDFC()
hdfc.hd_cash()

#Father --> Kid Property 
#In this case we will have constructor only in parent class
class Father:
    """Father class will have some property value"""
    def __init__(self):
        self.property = 5000000
    def father_property(self):
        print(f'Father property value is {self.property}')
class Kid(Father):
    #pass
    def __init__(self):
        self.property = 100000
    def kid_property(self):
        print(f'Kid own property is {self.property}')
        print(f'Kid Final property is {self.property + self.property}') 
value = Kid()
print(value.property1)
value.father_property()
value.kid_property()

trying by changing atrribute names

class Father:
    """Father class will have some property value"""
    def __init__(self):
        self.property = 5000000
    def father_property(self):
        print(f'Father property value is {self.property}')
class Kid(Father):
    #pass
    def __init__(self):
        self.property1 = 100000
    def kid_property(self):
        print(f'Kid own property is {self.property1}')
        print(f'Kid Final property is {self.property1 + self.property}') 
v = Kid()
print(v.property1)
#print(v.kid_property()) #Attribute Error as Overriding is happened


In above case Parent class constructor has been overriden by child class constructor
Constructor Overriding -->super()
super().__init__() #calls superclass constructor
super().__init__(args) #calls superclass constructor with arguments
super().method() #calls superclass method

class Father:
    """Father class will have some property value"""
    def __init__(self):
        self.property = 5000000
    def father_property(self):
        print(f'Father property value is {self.property}')
class Kid(Father):
    #pass
    def __init__(self):
        super().__init__() #calling superclass constructor
        self.property1 = 100000
        #super().__init__()
    def kid_property(self):
        print(f'Kid own property is {self.property1}')
        print(f'Kid Final property is {self.property1 + self.property}') 
value = Kid()
print(value.property)
print(value.property1)
value.kid_property()

#Calling Superclass constructor with arguments
class Father:
    """Father class will have some property value"""
    #def __init__(self,property):
        #self.property = property
    def __init__(self,property=1000000):
        self.property = property
    def father_property(self):
        print(f'Father property value is {self.property}')
class Kid(Father):
    #pass
    def __init__(self,property1,property):
        super().__init__(property) #calling superclass constructor with arguments
        self.property1 = property1
    def kid_property(self):
        print(f'Kid own property is {self.property1}')
        print(f'Kid Final property is {self.property1 + self.property}')
val = Kid(200000,500000)
print(val.property)
val.father_property()
print(val.property1)
val.kid_property()
f = Father()
f.father_property()
g = Kid(200000,property=450000)
g.kid_property()

#Area Calculation scenario

class Square:
    """Square Area Calculation with Constructor and Method Overriding"""
    def __init__(self,x):
        self.x = x
    #Instance Method
    def area(self):
        print(f'Area of Square is {self.x * self.x}')
class Rectangle(Square):
    def __init__(self,x,y):
        super().__init__(x) #calling superclass constructor with args
        self.y = y
    #def rarea(self): #if method name is different we can get result
        #print(f'Area of Rectangle is {self.x * self.y}')
    def area(self): #but we want to have same name
        #super().area()
        print(f'Area of Rectangle is {self.x * self.y}')
        super().area() #calling superclass method (Method Overriding)
#cal = Rectangle(7,4)
#cal.area()
#cal.rarea()
x,y = map(float,input("Enter the values:").split(','))
result = Rectangle(x,y)
result.area()

Multiple Inheritance --> one child class acquiring properties from multiple parent class

class Baseclass_1:
    pass
class Baseclass_2:
    pass
class Dervied_class(Baseclass_1,Baseclass_2):
    pass

#Whatsapp Scenario

class Users:
    """Users with simple feature"""
    def send_message(self):
        print("Sending Message")
class Notifications:
    """Sending Notification"""
    def notification(self):
        print("Notification Sent")
class PremiumUsers(Users,Notifications):
    """Premimum User"""
    def premium(self):
        print("Accessing Premium Features")
user1 = PremiumUsers()
print(dir(user1))
user1.premium()
user1.notification()
user1.send_message()

#Multilevel Inheritance --> one class acquire properties from another

class GrandParent:
    pass
class Parent(GrandParent):
    pass
class Child(Parent):
    pass
'''
class Users:
    def make_calls(self):
        print("Making Video Calls")
class BusinessUsers(Users):
    def create_catalog(self):
        print("products available")
class VerifiedBusinessUsers(BusinessUsers):
    def verification_badge(self):
        print("Blue Tick Verified")
user1 = VerifiedBusinessUsers()
user1.verification_badge()
user1.create_catalog()
user1.make_calls()
user2 = BusinessUsers()
user2.create_catalog()
user2.make_calls()

