Python 3.11.9 (v3.11.9:de54cf5be3, Apr  2 2024, 07:12:50) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #TypeConversion -->Converting one type to another as Python by default follows Implict Type
>>> #int -->float,complex,bool
>>> #Every built-in datatype is a built-in function in Python
>>> age = 32
>>> b = float(age)
>>> b
32.0
>>> c = complex(age)
>>> c
(32+0j)
>>> d = bool(age)
>>> d
True
>>> bool(0)
False
>>> #0,None,'',[],(),{} -->False
>>> price = 45.23
>>> type(price)
<class 'float'>
>>> q = int(price)
q
45
r = complex(price)
r
(45.23+0j)
g = bool(price)
g
True
h = bool(price+age)
h
True
#Complex ->int,float,bool
a = 3+6j
type(a)
<class 'complex'>
data = int(a)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    data = int(a)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
data = float(a)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    data = float(a)
TypeError: float() argument must be a string or a real number, not 'complex'
data = bool(a)
data
True
a = bool(int(float(12)))
a
True
b = int(float(bool(13)))
b
1
#boolean -->int,float,complex
a = True
int(a)
1
float(a)
1.0
complex(a)
(1+0j)
int(False)
0
float(False)
0.0
complex(False)
0j
