'''
Polymorphism -->Method Overloading (Compile time polymorphism)
             -->Method Overriding (Run Time Polymorphism)
             -->Operator Overloading (__add__,__str__,__init__)
Abtraction --> ABC
Management System using OOP -->Assignment 
'''
#Method Overriding --> This happens when the child class and the parent class possess the
#same method name where we want to behaviour change for both child and parent classes..

#HotStar scenario --> Free User (can watch limited content with advertisements)
#                 --> Paid user (can watch premium content without advertisements)
#                 --> Premium User (watch live content without advertisements and premium content)

'''
class User:
    """Method Overriding scenario"""
    def watch(self):
        print(f'Watching basic content with advertisements')
class PaidUser(User):
    def watch(self):
        print(f'Watching premium movies without advertisements')
    #def paid_watch(self):
        #print(f'Watching premium movies without advertisements')
u1 = User()
u1.watch()
u2 = PaidUser()
u2.watch()
#u2.paid_watch()

#Different Subscription Plans
class Free_User:
    """Method Overriding with Hotstar scenario of Different Subscription Plans"""
    def watch(self):
        print(f'Watching Free Content with Advertisements')
class VIP_User(Free_User):
    def watch(self):
        print(f'Watching Premium Content without Advertisements')
class Premium_user(Free_User):
    def watch(self):
        print(f'Watching Live content and Premium Movies')
u1 = Free_User()
u1.watch()
u2 = VIP_User()
u2.watch()
u3 = Premium_user()
u3.watch()

#In above case as we have different objects same method will exhibit different behaviour
#but we want to access parent class method also instead of overridiing we use
#super().method()

class Free_User:
    """Method Overriding with Hotstar scenario of Different Subscription Plans"""
    def watch(self):
        print(f'Watching Free Content with Advertisements')
class VIP_User(Free_User):
    def watch(self):
        super().watch()
        print(f'Watching Premium Content without Advertisements')
class Premium_user(VIP_User):
    def watch(self):
        super().watch()
        print(f'Watching Live content and Premium Movies')
u1 = Free_User()
#u1.watch()
u2 = VIP_User()
#u2.watch()
u3 = Premium_user()
u3.watch()
'''

#Operator Overloading --> +,-,*,/
# (Magic methods / Dunder Methods)  
# __add__, __str__, __init__
'''
a = 15;b=25
print(a+b)

print(a.__add__(b)) #a is current object , b is other object
print(a.__add__(55)) 

a = 'codegnan';b = 'python'
print(a+b)
print(a.__add__(b))
print(a.__str__())

a = [1,2,3,4];b = [2,4,5]
print(a.__add__(b)) #merging
print(a.__len__()) #print(len(a))
print(a.__mul__(2)) #print(a*2)

#WatchHistory in Hotstar scenario

class WatchHistory:
    """Understanding Operator Overloading"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours
#a = WatchHistory(120)
#print(a)
user1 = WatchHistory(120)
print(user1.hours)
user2 = WatchHistory(100)
print(user1+user2) #here we are able to add both users watchhistory only because
#we have used __add__()

#If you dont use it as below it encounters TypeError
class WatchHistory:
    """Understanding Operator Overloading"""
    def __init__(self,hours):
        self.hours = hours
    def new(self,other): #here we are using different method
        return self.hours + other.hours
#a = WatchHistory(120)
#print(a)
user1 = WatchHistory(120)
print(user1.hours)
user2 = WatchHistory(100)
#print(user1+user2)  #raises TypeError

class WatchHistory:
    """Understanding Operator Overloading"""
    def __init__(self,hours):
        self.hours = hours
    def __add__(self,other):
        return self.hours + other.hours
    def __str__(self):
        return f'Watching content for {self.hours} hours'
    #def new(self):
        #return f'Watching content for {self.hours} hours'
user1 = WatchHistory(100)
user2 = WatchHistory(50)
print(user1.hours)
print(user1+user2)
#print(user1.new())
print(user1.__str__())
print(user2.__str__())
'''
#Abstraction --> It is the process of hiding unnecessary and only shwing required details
#use only with abc module (abstractmethod,ABC)
#Instagram --> Upload photo,upload video,make reel
import abc
from abc import ABC,abstractmethod
class Content(ABC):
    #@abstractmethod
    def upload(self):
        pass
class Photo(Content):
    def upload(self):
        print(f'Photo is Uploading')
        print(f'Compressing Photo')
        print(f'Uploaded Photo with effects')
class Video(Content):
    def upload(self):
        print(f'Video is uploaded')
        print(f'Encoding the video')
        print(f'Video compressed without losing quality and uploaded')
class Reel(Content):
    def upload(self):
        print('Adding Effects to the reel')
        print(f'Uploading the Reel')
        print(f'Reel is uploaded aling with tags')
contents = [Photo(),Video(),Reel()]
for content in contents:
    #print(content)
    content.upload()





