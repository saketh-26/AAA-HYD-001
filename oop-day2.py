'''
OOP  
Methods -> Instance methods,Class Methods,Static Methods
#usage of Constructor

class Employee:
    """Employee Class displaying details"""
    company = "Codegnan" #class attributes 
    def __init__(self): #Constructor
        self.name = input("Enter the Employee Name:")
        self.age = int(input("Enter the employee age:"))
        self.role = input("Enter the Employee Role:")
    #Instance Methods
    def display_details(self):
        print(f'Employee name is {self.name},age is {self.age} years old and role is {self.role}')
print(Employee.company)
emp1 = Employee()
print(emp1.company)
print(dir(emp1))
emp1.display_details()
print(emp1.__dict__)
#use Salary as another attribute and keep conditions as 
#salary -ve case,0 case
#salary <10000 --> Dept Frontdesk
#salary 10000 - 25000 --> Dept Admin
#salary >25000 -<50000 --> Dept Training

#using self to modify the attributes within class

class Product:
    platform = "Amazon" #class attribute
    def __init__(self,name,price,discount):
        self.name = name
        self.price = price
        self.discount = discount
    def display_item(self):
        print(f'Item is {self.name} and price is {self.price}')
    def apply_discount(self):
        self.price = self.price - (self.price * (self.discount/100))
        print(f'Final price is {self.price}')
obj1 = Product("Iphone",95000,15)
print(obj1.platform)
print(Product.platform)
obj1.display_item()
obj1.apply_discount()
print(obj1.__dict__)
'''
#Classmethod --> @classmethod
#Staticmethod --> @staticmethod

class Product:
    platform = "Flipkart"
    delivery_charges = 50
    def __init__(self,name,price):
        self.name = name
        self.price = price
    @classmethod
    def update_delivery(cls):
        cls.delivery_charges = 60
    def display_items(self):
        self.price = self.price + Product.delivery_charges
        print(f'Item is {self.name} and price is {self.price}')
    @staticmethod
    def free_delivery(price):
        return price >=35000
'''obj1 = Product("Oneplus",15000)
print(obj1.platform)
print(Product.delivery_charges)
#obj1.display_items()
Product.update_delivery() #here we are accessing the classmethod
print(Product.delivery_charges)
obj1.display_items()
print(obj1.__dict__)'''
obj1 = Product('laptop',45000)
obj1.display_items()
print(obj1.free_delivery(30000)) #in this case we  have given our desired price
print(Product.free_delivery(36000))
print(obj1.__dict__)

#Use Static and Class methods but make sure free delivery should be applicable when the price > 30000
#where delivery charges should be zero
#below 30000 delivery charge should be 60 as per Class variable update


