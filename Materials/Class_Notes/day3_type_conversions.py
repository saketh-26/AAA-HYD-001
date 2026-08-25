Python 3.11.9 (v3.11.9:de54cf5be3, Apr  2 2024, 07:12:50) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Tokens
>>> #Datatypes -->Numeric datatypes,Boolean datatype,Sequence datatypes (list,str,tuple)
>>> #Set datatype (set,frozenset),mapping datatype(dict),None
>>> #Sequence datatypes -->list,tuple,str
>>> #Every built-in datatype is a Built-in function
>>> #list ->Mutable,Ordered,Indexed and heterogenous Collection --> []
>>> #typeconversion of int,float,complex,bool -->list
>>> age = 25
>>> type(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    type(a)
NameError: name 'a' is not defined
>>> type(age)
<class 'int'>
>>> b = list(age)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b = list(age)
TypeError: 'int' object is not iterable
>>> c = list(1,2,4,)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    c = list(1,2,4,)
TypeError: list expected at most 1 argument, got 3
c = list((1,2,4,))
c
[1, 2, 4]
price = 45.67
d = list(price)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d = list(price)
TypeError: 'float' object is not iterable
e = list(3+5j)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    e = list(3+5j)
TypeError: 'complex' object is not iterable
f = list(True)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    f = list(True)
TypeError: 'bool' object is not iterable
#tuple --> Immutable,Ordered,Indexed collection
#we use () as notation
#int,float,complex,bool -->tuple
temp = 1.4
tuple(temp)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(temp)
TypeError: 'float' object is not iterable
tuple(23)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(23)
TypeError: 'int' object is not iterable
tuple(2,3,4)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(2,3,4)
TypeError: tuple expected at most 1 argument, got 3
tuple(2+4j)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(2+4j)
TypeError: 'complex' object is not iterable
tuple(False)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(False)
TypeError: 'bool' object is not iterable
tuple(None)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    tuple(None)
TypeError: 'NoneType' object is not iterable
#str datatype
value = 45
b = str(value)
b
'45'
print(b)
45
type(b)
<class 'str'>
#In above case it has returned a Numeric String
discount = 1.5
a = str(discount)
a
'1.5'
c = str(1+3j)
c
'(1+3j)'
d = str(True)
d
'True'
type(d)
<class 'str'>
#string -->Immutable,Ordered and Indexed Collection
#Set datatype -->set(),Mapping -->dict()
age = 12
b = set(age)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    b = set(age)
TypeError: 'int' object is not iterable
c= set(2.3)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    c= set(2.3)
TypeError: 'float' object is not iterable
set(3+4j)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    set(3+4j)
TypeError: 'complex' object is not iterable
set(False)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    set(False)
TypeError: 'bool' object is not iterable
#mapping -->dict -->key value pairs -->Ordered,Mutable collection
a = 24
b = dict(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    b = dict(a)
TypeError: 'int' object is not iterable
