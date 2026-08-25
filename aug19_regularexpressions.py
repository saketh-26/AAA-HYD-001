'''
Tokens --> Operators,Datatypes --> Control Flow Statements -->POP -->Modules--> OOP
Regular Expressions --> Data Analysis (numpy,pandas,data visualization) --> Web Scraping & Virtual Assistant
'''
#Regular Expressions --> It is a special sequence of characters which helps in pattern matching,it helps 
#to match,search,find,extract or replace given pattern.It is widely used in Text Processing,Text Analysis,
#Web Development,AI.In Python it is available as re module

import re
'''
#we use representation as r'
a='\n'
print(a)
b = r'\n' #here we have used the reprsentation of raw string r' \n is treated as a character of (\ and n)
print(b)
print(len(b))'''
print(dir(re))
#search(),match(),findall(),compile()......
'''
#for suppose you have received order as Order ID : 34512
string = "Order ID :34512"
result = re.search(r'\d',string)
print(result)
print(result.group())
result = re.search(r'\d+',string) #\d matches digit, #+ is for matching one or more times occurance
print(result)
print(result.group())

#Extract the age of user from the data
data = "My name is Rahul and my age is 25,I live in Hyderabad"
age = re.search(r'\d+',data)
print(age) #it returns the matching object
print(age.start()) #it returns the start of matching object
print(age.end()) #it returns the end of matching object
print(age.span())
print(age.group()) #it returns the complete matched object
'''
#re.match() --> it is used to match only the beginning pattern

#greeting = "Hello Agents"
greeting = "Good Afternoon guys"
'''result = re.match(r'Hello',greeting)
print(result) #it returns None for unmatched object
if result:
    print(f'Matching is found : {result.group()}')
else:
    print("Match not Found")
#re.search() --> it checks for the first matched pattern
f = re.search(r'[A-Z]',greeting)
print(f)
print(f.group())
g= re.search(r'[A-Z]\w',greeting)
print(g)
h= re.search(r'[A-Z]\w+',greeting)
print(h)
print(h.group())
j= re.search(r'[a-z]\w+',greeting)
print(j)
print(j.group())
j= re.search(r'[a-z]+',greeting)
print(j)
print(j.group())

#re.findall() -->search all the matching pattersn and returns a list
f = re.findall(r'[A-Z]\w+',greeting)
print(f)
f = re.findall(r'[A-z]\w+',greeting)
print(f)
data = "Python 35 Agents 25 GENAI"
#result = re.findall(r'[A-z]\w+',data)
result = re.findall(r'[A-Z][a-z]+',data)
print(result)

#re.finditer() --> match the complete iteration along with position

ids = '23 45 36 codegnan' 
g = re.finditer(r'\d+',ids)
#g = re.search(r'\d+',ids)
#g = re.findall(r'\d+',ids)
#print(g)
#print(type(g))
for i in g:
    #print(i)
    print(i.group(),i.start(),i.end())
#print(*g)

#re.fullmatch() -->when we want to have the entire matching pattern to the complete string
data = "Codegnan is in Hyderabad,Vijayawada & Vizag,contact number is 8106429771"
#result = re.fullmatch(r'\d{2}',data) #needs pattern applicable for entire string it returns None
result = re.fullmatch(r'\d{10}','8106429771')
#result = re.findall(r'\d{10}',data)
print(result)
print(result.group())'''

#res.sub() -->where can replace the original pattern
#re.split() --> we can specify the split pattern

f = "I love Food codegnan Food sjasdjakhsjkahs Food"
g = re.sub(r'Food','Agents',f)
print(g)
h = re.sub(r'\s','*',f) #\s -> space character
print(h)

g = "Agents,GENAI;RAG,Python"
k = re.split(r'[,;]',g)
print(k)



