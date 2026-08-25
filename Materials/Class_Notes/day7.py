'''

Sequence Types --> Lists -->Mutable,Indexed,Ordered and Heterogenous Collection
Nested Lists -->List inside another lists
'''
data = ['codegnan',35,4.56,['Python','Java','AAI','DA'],100,45]
#print(data)
#print(len(data))
'''#We need to access inner list as below
print(data[3])
#now i want to get 'Python' and 'Java' from above list
a = data[3][:2]
print(a)
b = data[3][2:]
print(b)
#get only 'Pyt' as output
d = data[3][0][:3]
print(d)
#get the output as ['Python','AAI']
e = data[3][::2]
print(e)
#get the output as [35,['Python','Java','AAI','DA'],45]
f = data[1::2]
print(f)'''

#Lists are Mutable -->we can insert/remove elements
data = ['codegnan',35,4.56,['Python','Java','AAI','DA'],100,45]
#Using Indexing and Slicing ->change
#35 -->45
'''data[1] = 45
print(data)
print(len(data))
data[2] = ['Agents','Prompt','RAG']
print(data)
print(len(data))
data[3][1] = 'rag'
print(data)'''
#Indexing will never change the length of collection
#now we will use Slicing
'''data[1:3] = ['Java','DSA']
print(data)
data[1:3] = ['RAG','MCP','Agents','LORA','GPT','SONET']
print(data)
data[3][1::2] = ['RAG','MCP']
print(data)

#Indexing,Slicing,striding can insert elements but we loose our original data
'''
#append(),extend(),insert()
#append() -->inserts only single object at the end of list / empty list we can start assigning using it
#length will be incrementally increased
details = ['Saketh',32,'Codegnan']
print(len(details))
print(details)
'''
details.append(34)
print(details)
details.append('Agentic AI')
print(details)
details.append(data)
print(details)
print(details.append('Saketh')) #it returns None as we need to print only list
print(details)

age = []
age.append(32)
age.append(21)
age.append(22)
print(age)
'''

#extend() --> inserts multiple objects(iterable) to the end of the list
#details.extend(34,45)#TypeError
#print(details)
'''
details.extend((34,45))
print(details)
details.extend('codegnan') #it splits into characters
print(details)
details.extend(['codegnan'])
print(details)

print(data)

#insert() -->inserts object before index
details.insert(1,'Python')
print(details)
print(len(details))
details.insert(5,'Agents')
print(details)
details.insert(6,['Temperature','Agents'])
print(details)
details.insert(-1,'Codegnan')
print(details)

details[-1].append('Saketh')
print(details)
details[-1].extend(['RAG','MCP'])
print(details)
details[-1].insert(1,'Claude')
print(details)
'''
details.extend(['Agents','MCP'])
print(details)
#pop(),remove(),clear()
'''#pop() removes by default last index if not given
details.pop()
print(details)
details.pop(1)
print(details)

details.remove('Agents') #removes first occurance of a value
print(details)

details.clear() #removes all objects in the collection and returns empty list
print(details)

#to extract group of objects --> del
del details[2:4]
print(details)

del details #removes complete list
#print(details)

details.extend(['Agents','RAG'])
print(details)
#index(),count(),copy(),sort(),reverse()
print(details.index('Agents'))
print(details.index('Agents',4))
print(details.count('Agents'))
print(details.count('Qwerty'))
#print(details.index('Qwerty')) #ValueError as count = 0

#details.sort()
#print(details) #it is not possible
details.pop(1)
print(details)
details.sort()'''
#print(details) #alphabetical order as we have strings in it
b = [12,-98,23,78,2]
'''b.sort()
print(b)
b.sort(reverse = True) #this becomes descending order
print(b)'''
b.reverse() #b[::-1]
print(b)

#copy() ->creates a shallow copy of list
c = b.copy()
print(c)
c[2] = 'codegnan'
print(c)
print(b)

#Create nested list and observe copy() in it


















































































