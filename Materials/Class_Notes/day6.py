#Operations on Strings
#Case Conversions,Searching,Validation (Boolean value)...

#Searching and Finding methods -->find(),index(),count()

place = 'Hyderabad'
'''print(len(place))
print(max(place))
print(ord('A'))
print(ord('a'))
print(place)

#find() #first occurance of given character
print(place.find('d')) #it returns first occurance --> 2
print(place.find('a'))
print(place.find('Z')) #if unmatched char is present it returns -1

print(place.find('d',3)) #we can give the start index for a repeating char to find next position
print(place.find('a',6))

#rfind() -->will give last occurance
print(place.rfind('d'))
print(place.rfind('w')) #same it returns -1 as no character
'''
print(place)
'''
#index() #returns the first matching position of given object
print(place.index('e')) #it returns given char position
print(place.index('d'))
print(place.index('d',3))
#rindex() -->returns the last matching position
print(place.rindex('d')) 
print(place.index('Z')) #raises ValueError whereas find returns -1

#count() --> returns the number of occurances

print(place.count('d'))
print(place.count('d',3))  #it returns 1 as we have given specific index position to start counting

print(place.count('q')) #it returns 0 as we dont have such char
'''

#Testing Methods -->return Boolean value
#print(place)
'''
print(place.isupper()) #returns True if complete string is in uppercase
print(place.islower())
print('codegnan'.islower())
print(place.isalpha()) #returns True for an alphabetic string
print('code123'.isalpha()) #as it is alnum string
print('code123'.isalnum()) #returns True for an alphanum string
print('code 123'.isalnum()) #returns False

print('12345'.isalnum()) #returns True as we have digits also
print('12345'.isdigit())

print(place.startswith('H'))
print(place.startswith('d'))
print(place.startswith('d',2))
print(place.endswith('d')) #returns True

#print(place.istitle('H')) #raises an Error we need not pass any arguments
print(place.istitle())
print('Agentic ai'.istitle())


#Space removal (Trimming) methods -->strip(),lstrip(),rstrip()
#strip() -->removes both leading and trailing spaces

data ="Agents "
print(len(data))
f = data.strip()
print(f)
print(len(f))

a = ' codegnan '
print(len(a))
b = a.lstrip()
print(len(b))
c = a.rstrip()
print(len(c))
d = a.strip()
print(len(d))

#replace(),split(),join()
b = place.replace('e','f')
print(b)
c = 'codegnan agentic ai'.replace('a','policy')
print(c)
c = 'codegnan agentic ai'.replace(' ','') #we are replacing space with empty string
print(c)
d = 'saketh@codegnan.com'.replace('@','')
print(d)

#split() lets recap
data = input("Enter:").split(',')
print(data)

d = 'code,python,ai'
print(len(d))
d = 'code,python,ai'.split(',') #returns list as result but uses given separator
print(d)
print(len(d))

#join() #joins elements with given separators or chars...

a = 'code'
b = 'gnan'
c = a.join(b)
print(c)
print('#'.join('code'))
print('$$'.join('#'))
'''

#Sequence datatypes -->Lists [] -->Mutable,Ordered,Indexed,Heterogenous

age = [21,20,22,32]
print(age)
print(type(age))
print(len(age))

details = ['saketh',32,'python',3.56]
print(len(details))
print(type(details))
print(details[2])
print(details[-3])

#we need to extract 'hon' from above list
print(details[2])
print(details[2][3:])

print(details[::-1])
print(details[2:])

#Indexing and Slicing to be worked out....
#output -->['saketh','python']
#output -->[32,3.56]

#Merging/Concatenation,Repetition on Lists
print(age + details) 
print(age * 2)




































































































































































