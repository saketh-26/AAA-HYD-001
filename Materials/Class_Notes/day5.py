
#Sequence Datatypes -->Strings -->Group of characters,enclosed in single,double or triple
#quotes.Immutable,Ordered and Indexed Collection
"""
name = 'Saketh'
name = "Saketh"
name = '''Saketh'''

print(name)
#Access the number of objects in a collection --> len()
print(len(name))
print(len('Saketh AAA'))
#to access the type of object
print(type(name))

print(type('name'))

roll_no ='11Qk1A0433' #Alphanumeric String
print(len(roll_no))

mobile_no = '8106429771' #Numeric String
print(len(mobile_no))

#Operations on Strings ->Repetition,Concatenation,Indexing,Slicing,Membership..

#Concatenation (Merging) -->Combine multiple strings (+)
place = "Hyd";course = "AAA";name = "Codegnan"
print(name + course + place) #Concatenation
#You want to modify the output
print(f'We are in {course} class in {name} branch in {place}')

print('Codegnan'+':'+'Hyd'+'\t'+'Agentic AI')
#Repetition ->we use * operator 

data = 'Agent'
print(data*3)
#print(data + 3) it raises TypeError as String and string only can be concatenated
print('*' * 25)

#Membership --> in,not in
print('code' in 'codegnan')
print('agent' not in 'Generative AI')

#Indexing -->We can access position of an object in a string,we use [] to get the index of
#an object,it starts with 0 and ends at len(obj) - 1

name = 'codegnan'
print(len(name)) #--> returns 8

print(name[0]) #returns first character
print(name[6]) #returns sixth indexed position character
print(name[34]) #IndexError

print('agent'[2])

#Negative Indexing -->starts from last --> -1
name = "Codegnan"
print(name[-1]) #returns last character --> 'n'
print(name[-4])
print(name[4])
"""
#Strings are Immutable
name = "Codegnan"
#name[5] = 'p' #item assignment is not possible
#print(name)
'''
#Slicing -->Accessing group of characters -->[start:end] start will be included,end
#will be excluded

print(name[:])
print(name[1:]) #includes starting
print(name[1:5]) #both start and end
print(name[:5]) #only end
print(name[4:45]) #even though end is of out of range it returns till end of string

print(name[5:])
print(name[5:1]) #not at all possible,as in positive slicing we can access only from lower
#index to higher index

print(name[-5])
print(name[-5:]) #it starts from last 5th character
print(name[-5:-1]) #remember lower to higher
print(name[-1:-5]) #returns empty string
print(name[:-8]) #returns empty string
print(name[-8:]) #returns complete string

#[::] -->[start:end:step]
print(name)
b = name[::]
print(b)
print(b[::1]) #it also returns complete string
#we can give our desired +ve interval

print(b[::2])
print(b[1:7:3])
print(b[2:9:5])
print(b[:4:5])
print(b[1::4])

print(name)

print(name[::-1]) #prints in reverse order
print(name[::-2])
print(name[::-6])

print(name[-8:-1:]) #returns complete excluding last character
print(name[-8:-1:-2]) #returns empty string as no possibilities
print(name[-8:-1:2])
print(name[1:7:-1])

#Built-in functions -->len(),type(),min(),max(),ord(),chr()

#place = 'hyderabad'
place = 'Hyderabad'
print(len(place))
print(type(place))
print(min(place)) #returns 'H' as per ASCII values
print(max(place))

print(ord('A')) #returns ASCII value of given character

print(chr(97)) #returns specific character as per ASCII value
'''
#Methods(Functions) on strings

#Case Conversions --> converting from one case to another
#lower(),upper(),title(),capitalize(),swapcase()

course = "Agentic ai"
print(course)
print(course.lower()) #converts to lower case
print(course.upper()) #converts to uppercase
print(course.swapcase())
print(course.title()) #first letter of every word will be capitalized
print(course.capitalize()) #first letter will be capitalized


















































































