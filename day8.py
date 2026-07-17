'''
Tuples --> Tuples are an Immutable,Ordered,Heterogenous,
Indexed Sequence Type,we use () for declaration
'''
data = 1,24,5
print(data)
print(type(data))

#Nested Tuples and also have lists inside it
details = ('codegnan',32,(2,4,5),'saketh',[12,45,'agents','rag'])
print(details)
'''print(len(details))
print(details[2]) #it returns tuple as output
print(details[4][2])

#my output should be as below
#('codegfaf',32,(2,4,5),'saketh',[12,45,'agents','rag'])

print(details[0])
details[0] = details[0].replace('n','f') #Tuples are immutable we cant modify it
print(details)

details[4][2] = details[4][2].replace('a','A')#here we are using lists so its mutable
print(details)
print(details[1:4])

print(details[::3])
#Practice urself indxing,slicing and striding
print(type(details[4])) #always use type() 
details[4].remove('agents')
print(details)

#Operations on Tuples ->Indexing,SLicing,Membership,Concatenation/Merging,Repetition
age = 22,21,32,25
ids = 231,342,213
print(age + ids) #merging
print(age * 2)
print(22 in age) #membership

#len(),type(),min(),max(),sorted()[returns sorted elements in list you can typecast it]
age = (25,12,45,65)
print(min(age))
print(max(age))
print(tuple(sorted(age))) #Typecasting

#index(),count()
details = ('saketh','codegnan','Agentic AI',34,23,5.8)
print(details)

print(details.index(34))
print(details.count(34))

#Tuple ->List..(Typecasting)
details = list(details)
print(details)
print(type(details))

#convert string to List/Tuple

data = 'AgenticAI'
print(type(data))
data = list(data)
print(len(data))
print(data)
data = tuple(data)
print(data)

#Set Datatype -->Sets,Frozen Sets

#Sets --> A Set is a Unique,Mutable collection -->set(),Unordered
a = {} #by dfault it is empty dictionary
b = set()
print(type(a))
print(type(b))

ids = {123,124,125,126,127,123,124}
print(ids)
print(len(ids))
'''
#data = {23,4.5,'codegnan',{12,34,5}} #A set cannot contain a list and a set inside it
#print(data)
#As Set is Mutable we can insert,remove elements into a set

ids = {123,124,125,126,127,123,124}
#print(ids)
'''#add(),update()
ids.add(156)
print(ids)
ids.add('agents')
print(ids)
#ids.add(ids)
#print(ids)
ids.update(ids)
print(ids)
ids.update(['saketh','codegnan',124,256])
print(ids)
details = ['Siva','Sam','Ram','Ajay']
ids.update(details)
print(ids)'''

#remove elements from a set ---> discard(),remove(),clear(),pop()
'''
ids.discard(123)
print(ids)
ids.remove(124)
print(ids)

#ids.remove(123) #returns KeyError
#print(ids.discard(123)) #discard will avoid error

print(ids.pop()) #removes and returns an arbitrary elemt from a set
print(ids.pop())
print(ids.pop())
#print(ids.pop()) it has become empty set 

#clear() removes all elements and returns an empty collectn
print(ids.clear())
print(ids) #returns empty set

#Union,Intersection,Difference,Symmetric Difference,Subsets,Supersets

ages = {35,23,123,24,45}
print(ages)
d = ids.union(ages)
print(d)
e = ids.update(ages) 
print(e) #here it rturns None as update is happening in ids set 
print(ids)

f = ids.intersection(ages)
print(f)
g = ids.intersection_update(ages) 
print(g)
print(ids) #picks common elements from both sets and updates the first set

h = ids.difference(ages)
print(h) #removes common elemnts and returns rmng elements from frst set

# |(Union) , &(Intersection) , - (Difference),^ (Symmetric difference)
g = ages - ids
print(g)
u = ids | ages
print(u)
j = ages.symmetric_difference(ids) #removes common elements and returns elmnts from all rmng
print(j)

a = {1,2,3}
b = {1,2,3,4,5}
#below functions will return boolean
print(a.issubset(b)) #all elements of set a are present in set b
print(b.issuperset(a))
print(a.isdisjoint(b)) #it returns False as set a is already a subset of set b
'''
#Frozenset --> Immutable set
data = frozenset(ids)
print(data)
print(type(data))

#we cannot insert/remove elements but mathematical operations are possible
temp_details = frozenset([34,35,34,32,31])
print(temp_details)
print(min(temp_details))
print(max(temp_details))
print(sorted(temp_details))


#Hometask -->Practice on Lists and sets create a nested sequence include a list with tuples,
#set and strings...

















































