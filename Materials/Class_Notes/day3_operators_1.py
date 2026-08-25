Python 3.11.9 (v3.11.9:de54cf5be3, Apr  2 2024, 07:12:50) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Operators -->Operators are special symbols or keywords which performs specific operations on operands
#Arithmetic,Assignment,Comparision,Membership,Identity,Logical and Bitwise Operators
#Arithmetic Operators --> +,-,*,/(Float Division),// (Floor Division),%(modulus),**(exponentiation)
age = 12+2
age
14
b = 23
c = b-age
c
9
a*b
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a*b
NameError: name 'a' is not defined
age*b
322
d = age/c
d
1.5555555555555556
b = (2+3*6)
b
20
4/2
2.0
1/1
1.0
0/0
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    0/0
ZeroDivisionError: division by zero
0?5
SyntaxError: invalid syntax
0/3
0.0
#Floor Division -->It always return integer (quotient value as output)
4 // 2
2
5 // 2
2
9// 2
4
#Modulus --> % which returns remainder
9 % 2
1
4 % 2
0
12345 % 123
45
#Exponential --> **
2 ** 2
4
3 * 2
6
3 ** 2
9
3 x 2
SyntaxError: invalid syntax
3 'X' 2
SyntaxError: invalid syntax
'codegnan' * 2
'codegnancodegnan'
'code' + 'gnan'
'codegnan'
value = 123 + 2.3 + True + (2+5j)
value
(128.3+5j)
>>> d = 1.2 * False
>>> d
0.0
>>> #Assignment Operators
>>> # =, +=,-=,*=,/=,//=,**=
>>> d = 23
>>> d
23
>>> d += 34  #+= Addition Assignment operator --> d = d + 34
>>> d
57
>>> d += 5
>>> d
62
>>> d -= 5
>>> d
57
>>> d =- 3
>>> d
-3
>>> d++
SyntaxError: invalid syntax
>>> d++2
-1
>>> #Comparision (Relational Operators)
>>> # ==, != , < , >, <=, >=
