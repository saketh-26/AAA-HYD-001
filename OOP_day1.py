'''
Tokens --> Datatypes -> Control Flow --> Functions --> Modules 
Procedural Oriented Programming --> Functions

Object Oriented Programming --> objects --> It organizes the data and makes use of it using 
objects 
An object is real world entity --> Attributes (data), Methods (behaviour) Functions

class Class_Name:
    attributes...(variables)
    .........
    .........

    def fname(self): #behaviour 
        """Doc String"""
        .....
        ......
obj = Class_Name()..

#Wooden chair --> chair as object,class (blueprint which includes complete measurement
dimensions),carpenter -->User,Scrap materials,wood --> Memory

#Resuablity,Modularity,Abstraction,Encapsulation,Inheritance,Polymorphism

class Product:
    """Simple class demonstration with Ecommerce Example"""
    platform = "Amazon" #class Attribute
    def display_product(self):
        print(f'Displaying Products')
    def stock_available(self):
        print(f'Stock is available')
laptop = Product()
print(dir(laptop))
print(laptop.platform)
laptop.display_product()
laptop.stock_available()
Mobile = Product()
Mobile.display_product()
#Product -->Class,platform -->attribute,display_product,stock_available -->methods..

class Product:
    """Usage of class with instance attributes"""
    platform = "Amazon" #class attribute
    def store_products(self,name,price):
        self.name = name
        self.price = price
    def display_products(self):
        print(f'Product name is {self.name}')
        print(f'Product price is {self.price}')
Mobile = Product()
print(dir(Mobile))
Mobile.store_products("Iphone",55000)
print(Mobile.name)
print(Mobile.price)
Mobile.display_products()
Mobile2 = Product()
Mobile2.store_products("One Plus",35000)
Mobile2.display_products()
print(Mobile.platform)
print(Mobile2.platform)

#Take dynamic data from user and make sure to create 5 products
for i in range(2):
    n= input("Enter the Product name:")
    p = float(input("Enter the Product Price:"))
    Mobile = Product()
    Mobile.store_products(n,p)
    Mobile.display_products()
    print(Mobile.__dict__)

class Students:
    """Student details of AAA Batch"""
    batch = "AAA-HYD-001" #class attribute
    def student_data(self):
        self.name = input("Enter the student name:")
        self.age = int(input("Enter the Age:"))
        self.place = input("Enter the place:")
    def details(self):
        print(f'Student name is {self.name}')
        print(f'Student is from {self.place} with age as {self.age} years old')
print(Students.batch)

Stud1 = Students()
print(Stud1.batch)
Stud1.student_data()
Stud1.details()
print(Stud1.__dict__)
print(Stud1.__doc__)
print(Stud1.__class__)
Stud2 = Students()
print(Stud2.batch)
Stud2.student_data()
Stud2.details()
print(Stud2.__dict__)
'''

#Usage of Constructor
class Students:
    """Student details of AAA Batch"""
    batch = "AAA-HYD-001" #class attribute
    def __init__(self,name,place,age):
        """Constructor usage"""
        self.name = name #instance attributes
        self.place = place
        self.age = age
    def details(self):
        print(f'Student name is {self.name}')
        print(f'Student is from {self.place} with age as {self.age} years old')
Stud1 = Students("Saketh","Hyd",21)
Stud1.details()
Stud2 = Students(place = "Vizag",name="Sai",age=21)
Stud2.details()
