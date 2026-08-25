Python 3.11.9 (v3.11.9:de54cf5be3, Apr  2 2024, 07:12:50) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Interpretor Mode
>>> #Programming --> Tokens (smallest units of Programming)
>>> #Tokens ->Keywords,Identifiers,Literals,Operators,Variables,Punctuators
>>> #Python is General Purpose as simple as English
>>> #Keywords are reserved words in Python
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()
Welcome to Python 3.11's help utility! If this is your first time using
Python, you should definitely check out the tutorial at
https://docs.python.org/3.11/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To get a list of available
modules, keywords, symbols, or topics, enter "modules", "keywords",
"symbols", or "topics".

Each module also comes with a one-line summary of what it does; to list
the modules whose name or summary contain a given string such as "spam",
enter "modules spam".

To quit this help utility and return to the interpreter,
enter "q" or "quit".

help> keywords

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

help> and
Boolean operations
******************

   or_test  ::= and_test | or_test "or" and_test
   and_test ::= not_test | and_test "and" not_test
   not_test ::= comparison | "not" not_test

In the context of Boolean operations, and also when expressions are
used by control flow statements, the following values are interpreted
as false: "False", "None", numeric zero of all types, and empty
strings and containers (including strings, tuples, lists,
dictionaries, sets and frozensets).  All other values are interpreted
as true.  User-defined objects can customize their truth value by
providing a "__bool__()" method.

The operator "not" yields "True" if its argument is false, "False"
otherwise.

The expression "x and y" first evaluates *x*; if *x* is false, its
value is returned; otherwise, *y* is evaluated and the resulting value
is returned.

The expression "x or y" first evaluates *x*; if *x* is true, its value
is returned; otherwise, *y* is evaluated and the resulting value is
returned.

Note that neither "and" nor "or" restrict the value and type they
return to "False" and "True", but rather return the last evaluated
argument.  This is sometimes useful, e.g., if "s" is a string that
should be replaced by a default value if it is empty, the expression
"s or 'foo'" yields the desired value.  Because "not" has to create a
new value, it returns a boolean value regardless of the type of its
argument (for example, "not 'foo'" produces "False" rather than "''".)

Related help topics: EXPRESSIONS, TRUTHVALUE

help> 2+3
No Python documentation found for '2+3'.
Use help() to get the interactive help utility.
Use help(str) for help on the str class.

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
#Identifiers
#variables,datatypes,functions,classes,objects...
#You can use uppercase,lowercase but cannot start with numbers and special characters but you can have underscore also as an Identifier
email_id = "saketh@codegnan.com"
temperature = 0.3
$temp = 1.4
SyntaxError: invalid syntax
my name = 'codegnan'
SyntaxError: invalid syntax
12ert = 23
SyntaxError: invalid decimal literal
_ =12
_
12
False
False
False = 'code'
SyntaxError: cannot assign to False
#Variables -->Storageholders
name = "codegnan"
name
'codegnan'
NAME
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    NAME
NameError: name 'NAME' is not defined
'
#Python is Case-Sensitive
&name = 'saketh'
SyntaxError: invalid syntax
if = 23
SyntaxError: invalid syntax
name
'codegnan'
name = 23
name
23
#Operators
#+, _ , =,+=,<,>
#Literals --> Constant values assigned to variables
pi = 3.14
age = 32
place = 'codegnan'
#Punctuators --> [],(),{}.....
age = 10
age + 23
33
import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
#Multiassignment,Swapping,Deleting variables
age = 32
age
32
a,b,c = 12
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    a,b,c = 12
TypeError: cannot unpack non-iterable int object
a,b,c = 12,2.3,'codegnan'
a
12
b
2.3
c
'codegnan'
name,age,place = 'Codegnan',7,'Hyderabad'
name
'Codegnan'
age
7
place
'Hyderabad'
a = b = 23
a
23
b
23
#In above case we are assigning same value
#Swapping variables
a,b
(23, 23)
b = 25
a
23
b
25
a,b = b,a
a
25
b
23
c,d = b,a
c
23
d
25
e
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    e
NameError: name 'e' is not defined
#Deleting variables
del
SyntaxError: invalid syntax
del a
a
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    a
NameError: name 'a' is not defined
b c d
SyntaxError: invalid syntax
print(b,c,d)
23 23 25
del b,c,d
print(b,c,d)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    print(b,c,d)
NameError: name 'b' is not defined
#Statements
age = 32
#age = 32
#Comments --> Single Line Comments #
#MultiLine COmments --> Triple Quotes """ / '''

=================== RESTART: /Users/sakethkallepu/Documents/game.py ==================
