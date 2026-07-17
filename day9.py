'''
Datatypes --> Numeric,boolean,None,Sequence datatypes (str,lists,tuples),Set datatype(Sets
Frozen sets),Mapping (Dictionary)
'''
#Dictionary --> Collection of key-value pairs,Mutable,Ordered.. --> {},dict()

'''details = {}
print(details)
print(type(details))

details = {'Name':'Codegnan','Place':'Hyd','age':7}
print(details)
print(len(details))
#Accessing keys
print(details['Name'])
#print(details['Age']) #raises KeyError

#keys must be unique in a dictionary

data = {'Age':25,'name':'code','Age':26}
print(data) #here recent update value of Age will be taken
#in dictionary we index by using keys
'''

#Create Dictionaries using other datatypes

students_data = {'ids':[23,21,45,52],
                 'names':['Praneeth','Abhiram','Vasanthi','Akshitha'],
                 'place':('Hyd','Vjwda'),
                 'gender':{'male','female'}}
'''print(len(students_data))
print(students_data.keys()) #return keys from dictionary
print(students_data['names'])

print(students_data.values())

#Updating Dictionary
students_data['Course'] = ['PFS','JFS','AAA','DA']
print(students_data)
print(students_data)
print(type(students_data))

print(type(students_data['ids']))
#now if we want to insert 3 more unique ids
#students_data['ids'] = 56,67,87 #this is not recommended in this case

#print(students_data)
students_data['ids'].extend([56,67,87])
print(students_data)

students_data['names'].insert(1,'Ashok')
print(students_data['names'])

#We want to insert new place
students_data['place'] = list(students_data['place'])
print(students_data['place'])
#students_data.append('Vizag')
students_data['place'].append('Vizag')
print(students_data['place'])
students_data['Course'] = ['PFS','JFS','AAA','DA']
print(students_data)

#print the below outputs
#['JFS','DA'] do in a single step
#[23,52, 56, 67, 87] your ids should be as shown
#we need to sort the names

students_data['names'].sort()
print(students_data['names'])

#keys(),values(),items()
print(students_data.items()) #returns key,value pairs as tuple

#get will return value if key is existing,else default -->None
print(students_data.get('branch')) 
print(students_data.get('branch','CSE'))#returns 'CSE' instead of None
print(students_data.get('names'))
print(students_data)
#print(students_data['branch']) #raises KeyError as we dont have branch 

#setdefault() -> update the dictionary if key is not existing witjh default None
print(students_data.setdefault('ids'))
#students_data.setdefault('branch')
students_data.setdefault('branch',['CSE','CSD','ECE','IT'])
print(students_data)

#update(),pop(),popitem(),clear()
students_data.update({'fees':[456,234],'marks':[45,78,85]})
print(students_data)
print(students_data.pop('marks')) #we need to mention the key which we want to remove
print(students_data)
print(students_data.popitem()) #comes from the last
print(students_data)
#clear() and copy() work it out...

#fromkeys() will create a new dictionary by accpeting each object in the givn iterable as
#key whereas value is set to None
ids = [23,45,67]
#to convert above list to dictionary
d = dict.fromkeys(ids) #each value will be assigned as None we can modify accordingly
print(d)
d[23] = 'random'
print(d)

#print(d + d) #Not Possible for sets and dicts
#Membership --> in,not in (keys)
print(23 in d) #returns True as we have 23 as key
'''
#nested dictionaries :Dictionaries inside another dictionary

data = {
    's1':{'id':23,
          'name':'ram',
          'place':'hyd'},
    's2':{'id':25,
          'name':'sony',
          'place':'bng'}}
print(data.keys())
print(data['s1']['name'])
 
#Task -->Create a Nested dictionary with your own scenario


























