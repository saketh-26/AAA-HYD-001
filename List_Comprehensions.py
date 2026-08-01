'''
List Comprehensions --> In Python its a precise/easiest way to create Lists

Syntax : [expression for item in iterable]
iterable --> list,tuple,set,dict or range()

#We need to append elements into list
list = []
for i in range(10):
    list.append(i)
    #print(list)
print(list)

#the same above using List Comprehension
list = [i for i in range(10)]
print(list)

#Get the squares of numbers
data = [i**2 for i in range(10)]
print(data)

e = [i%2 ==1 for i in range(10)]
print(e)

#Converting strings to uppercase/lowercase
details = ['saketh','codegnan','data','agents','rag']
new = [i.upper() for i in details]
print(new)
print(*new)
a,b = 5,6

a,*name,c = 1,'saketh','codegnan','data',34
print(a)
print(name) #in this case we get a list
print(*name) #in this case all of those values are returned side by side
print(c)

a = [15,20,25,35]
#update the list with each value by 5
a = [i+5 for i in a]
print(a)

#get the first letter of each object in collection
data = ['codegnan','agents','rag']
letter = [i[0] for i in data]
print(letter)'''

#List Comprehension with if usage
# [expression for item in iterable/range if condition]

#Even numbers from the collection
#collection = list(map(int,input("Enter the values").split(',')))
#print(collection)
#result = [i for i in collection if i%2==0]
'''print(result)
for i in result:
    print(i,end=' ')
#by using filter() --> lambda
result1 = list(filter(lambda x:x%2==0,collection))
print(result1)

#fetch desired values with condition satisified
final = [i for i in collection if i >10]
print(final)

#List Comprehension with if-else condition
#Syntax:
# [true_value if condition else false_value for item in iterable]
data = [12,3,4,6,7,9]
print(data)
result = ["New" if i%2== 0 else "Old" for i in data]
print(result)

#Nested List Comprehensions 
#Nested -> one inside another  (one loop inside another loop)
#[expression for i in iterable1 for j in iterable2]

a = [(i,j) for i in range(5) for j in range(3)]
print(a)

b = [(i,j)for i in [1,3,5] for j in [4,5,6]]
print(b)

#Mutliplication table pattern
c = [i*j for i in range(1,11) for j in range(1,11)]
print(c)
print(*c)

colors =['Red','Blue','Green']
sizes =['S','M','L']
dress = [(i,j) for i in colors for j in sizes]
print(dress)

#Nested Comprehension with if condition 
#[expression for item1 in iterable1 for item2 in iterable2 if condition]

#Possible pairs
a = [(i,j) for i in range(5) for j in range(3) if i!=j]
print(a)

c = [i*j for i in range(1,11) for j in range(1,11) if i!=j]
print(c)
print(*c)

#Nested Comprehensions with if-else
#[true_value if condition else false_value for item1 in iterable for item2 in iterable]

a = [1,3,5,6,7]
b = [2,4,6,8,9]
c = [x+5 if x<y else x for x in a for y in b]
print(c)
'''
#In the above case if we replace [] braces with () we dont get tuple -->generator
#No Tuple Comprehension --> Generator
#Generator --> Generator is a Special Function which produces one value at a time..
#we use yield keyword
#Normal function
'''
def fname():
    """doc string"""
    return value(s)
fname()

def fname():
    """Doc String"""
    yield value1
    yield value2
    yield value3
fname()

def fun():
    """Normal Function"""
    return [1,2,4,5,6]
    #return "saketh"
print(fun())
a = fun()
for i in a:
    print(i)

def fun():
    """Generator function"""
    yield 1
    yield 2
    yield 3
#print(fun())
b = fun()
print(next(b))
print(next(b))
print(next(b))
print(next(b)) #StopIteration
'''

def display():
    """subjects covered"""
    yield "Python"
    yield "GENAI"
    yield "RAG"
    yield "Agents"
print(display())
print(type(display()))
d = display()
print(next(d))