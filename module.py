'''
Modules --> User Defined Module -->Create,Accessing 
Built-in Modules ->os,sys,random,math,platform,collections,itertools....

A Module is a Python file (.py),we use import keyword

import my_module
print(dir(my_module)) #use dir to get available methods and attributes
#Accessing from module

print(type(my_module.greet))
print(my_module.greet("Saketh"))
#print(my_module.names)
#print(type(my_module.names))

my_module.names.update({'place':'Hyd','age':7})
print(my_module.names)
print(type(my_module.display()))

#Accessing methods/attributes using from keyword 
#from my_module import greet
#print(greet("Agents"))
#print(names) #NameError as we didnot import 
from my_module import greet,names
print(greet("AAAI"))
print(names)
#print(display) #again it raises NameError 

#To access all methods/attributes we use *
#recommended only for userdefined/simple modules

from my_module import *
print(greet("Saketh"))
names.update({'course':"AAAI"})
print(names)
#print(display())
y = display()
print(next(y))
print(__name__)
print(__doc__)
print(my_module.__doc__)
print(my_module.__name__)

#Built-in Modules -->math,os,sys,random,json,collections,itertools
#math --> It has all mathematical constants,trigonometric functions and basic math functions

import math
#print(dir(math))
print(math.__doc__) #it gives description about the module
print(math.ceil(2.1)) #it returns the next higher value --> int
print(math.floor(2.9)) #it returns the lower value of given value --> int
print(math.e) #returns exponential value
print(math.exp(2))
print(math.factorial(6)) #returns the factorial of number
print(math.fmod(5,2)) #returns float value of modulus (5,2) 5%2 --> 1.0
print(math.log(2))
print(math.log10(2))
print(math.log2(2))
print(math.modf(5.3)) #separates the real and integral part
print(math.pi)
print(math.pow(5,3))
print(math.trunc(5.5))

#os,sys,random,json...
#os -->It provides functions to interact with operating system..

import os 
#print(dir(os))
#print(os.getcwd()) #returns current working directory
#change current directory
#os.chdir('/home/workspace/my-project/Python_Classes')
print(os.getcwd())
#print(os.listdir()) #returns list of all files in the directory
for i in os.listdir():
    print(i)
#print(os.mkdir('sample')) #make a directory
print(os.removedirs('sample')) #removes permanently

import sys
print(sys.path) #gives complete root path

#random module -->majorly useful to generate random data
import random,time
#print(dir(random))
#print(random.random()) #it gives random number (float)
#OTP Generation
for i in range(10):
    print(random.randint(1000,9999))
    time.sleep(5)

#JSON --> Encoding and Decoding (json) -->Python objects to JSON format and viceversa
#dumps() and loads()

import json
data = {'name':'Codegnan','age':7}
print(type(data))
parsed_data = json.dumps(data)
print(parsed_data)
print(len(parsed_data))
print(type(parsed_data))
result = json.loads(parsed_data)
print(result)
print(type(result))
sample = json.loads('[12,3,4,5]')
print(type(sample))
'''
#collections --> Counter,itertools -->combinations and permutations

from collections import Counter
data = ['A','B','C','A','A','C']
r = Counter(data)
print(r)
print(type(r))
h = dict(Counter(data))
print(h)
print(type(h))






















