'''
Inheritance -> Hierarchical Inheritance,Hybrid Inheritance

Hierarchical Inheritance --> It is a type of Inheritance where multiple child classes inherit properties
from single parent (base) class

class Parent:
    pass
class Child(Parent):
    pass
class Child2(Parent):
    pass
class Child3(Parent):
    pass
class Child4(Parent):
    pass..
    ....
....

#Whatsapp Scenario

class User:
    """User class with Message properties"""
    def send_message(self):
        print(f'Sending Messages')
class PersonalUser(User):
    """Personal User class inherting from User class"""
    def status_update(self):
        print(f'Status Updated only for Contacts')
class BusinessUser(User):
    """Business User"""
    def create_catalog(self):
        print(f'Catalog Creation is possible')
class VerifiedBusinessUser(User):
    """Verified User"""
    def premium_access(self):
        print(f'Blue Tick added,with premium features loaded')
user1 = User()
user1.send_message()
user2 = PersonalUser()
user2.send_message()
user2.status_update()
user3 = BusinessUser()
user3.create_catalog()
user3.send_message()
user3.status_update()

Hybrid Inheritance --> It is a type inheritance in which one or more than one type of inheritances 
can be applicable

class User:
    """User class with voice calls"""
    def voice_call(self):
        print(f'Making Voice call')
    def video_call(self):
        print(f'Making Video call')
class Notification(User):
    """Sending Notifications"""
    def notify(self):
        print('Sending Notification')
class BusinessUser:
    """Business User access"""
    def catalog(self):
        print(f'Catalog is updated')
class PremiumBusinessUser(BusinessUser,Notification):
    """Premium Content """
    def premium_access(self):
        print(f'Blue Tick Verification and Reach Access')
u1 = BusinessUser()
u1.catalog()
u2 = PremiumBusinessUser()
u2.premium_access()
'''
#Polymorphism --> feature of OOP
#Poly --> many
#morph --> forms
'''
Method Overloading --> Method with default arguments,Method with variable length arguments (*args),
Checking with variable length type
Method Overriding
Operator Overloading --> __add__,__str__

#HotStar --> FreeUser,Premium User,Adv Premium User

class HotStar:
    """Simple example to understand Polymorphism"""
    def watch(self):
        print(f'Welcome to HotStar Home page...Content Loading')
    def watch(self,movie):
        self.movie = movie
        print(f'Loaded Hotstar watching {self.movie}')
user = HotStar()
user.watch("Leo")
user.watch()

#Method Overloading with default arguments:
class HotStar:
    """MOverloadin with default argument"""
    def watch(self,movie=None):
        if movie==None:
            print(f'Welcome to Hotstar....')
        else:
            print(f'Watching {movie}')
user = HotStar()
user.watch()
user.watch("Vikram")
user.watch("Leo")

#Method Overloading with Variable length arguments usage

class HotStar:
    """method overloading with *args usage"""
    def add_to_watchlist(self,*movies):
        print(f'Movies Added')
        for movie in movies:
            print(movie)
user = HotStar()
user.add_to_watchlist('Leo','Vikram','Save the Tigers','Maa Inti Bangaram')
'''

#method overloading --> checking the type of arguemnts usage
#Hotstar --> one movie,multiple movies..

class HotStar:
    """checking the type of arguments usage"""
    def movies_list(self,content):
        if isinstance(content,str):
            print(f'Watching {content}')
        elif isinstance(content,list):
            print(f'Movies Added')
            for movie in content:
                print(movie)
user = HotStar()
user.movies_list("Vikram")
user.movies_list(['Leo','Vikram','Maa inti Bangaram'])








