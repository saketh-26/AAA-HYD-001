'''
TypeConversions ->list,tuple,set,dict

list -->str,tuple,set,dict

age = [23,21,43]
age = list((21,21,43))
print(type(age))
#Every built-in datatype is a built-in function
b = str(age)
print(b)
print(len(b))
c = tuple(age)
print(type(c))
d = set(age)
print(d)
#e = dict(age) raises TypeError
#print(e)
e= dict.fromkeys(age)
print(e)

#str -->list,tuple,dict
name = 'codegnan'
print(type(name))
g = list(name)
print(g)
h = name.split()
print(h)
j = name.split(',')
print(j)
e = dict.fromkeys(name)
print(e)

#Input Formatting --> List input,Tuple input,dict input --> eval()
#list as input
data = eval(input("Enter the list:"))
print(data)
print(type(data))
data = eval(input("Enter the tuple values:"))
print(data)
print(type(data))

details = eval(input("Enter the student details :"))
print(details)
print(type(details))
'''
#Repetition Statements (Loops) -->for , while
#loops will automate the tasks
'''
for loop is usedto iterate the items in a collection (str,list,tuple...) also can
generate a sequence of numbers (range)

syntax for :

for <loop_var> in collection/range_function:
    statement(s).....
    ......

marks = [24,25,21,20]
for mark in marks:
    print(mark)
    print(mark,end='\t')

#Find the Sum and Average of Marks

marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)
summ = 0; avg = 0
for i in marks:
    #print(i)
    summ = summ + i
    #print(summ)
    #avg = summ / len(marks)
    #print(avg)
print(f'Sum of given values is {summ}')
print(f'Avg of given values is {summ/len(marks)}')
#[1,3,4.5,'codegnan',3,'agents',2.4]
#find the sum of the above list

a = [1,3,4.5,'codegnan',3,'agents',2.4]
result = 0
for i in a:
    if type(i) in (int,float):
    if type(i) == int or type(i) == float:
        result += i
    print(result)
print(f'Sum is {result}')

details = {'names':['Sai','Abhi','Ram'],
           'marks':[24,20,28]}

print(details.items())        
for i in details:
    print(i)

for key in details:
    print(key)

for value in details.values():
    print(value)

for key,value in details.items():
    print(f'Key is {key}')
    print(f'Value is {value}')

#range(start,end,step) -->generates a sequence of values
#range(end) #by default start is 0
for i in range(5):
    #print(i)
    print(f'Value of i is {i}')
#range(start,end)
for i in range(1,11):
    print(i,end=' ')
#range(start,end,step)
for i in range(1,11,2):
    print(i)
#In same way return numbers in reverse order
#10 8 6 4 2 0
for i in range(10,-1,-2):
    print(i)


#Home task print below patterns

#A B C D E F G H

#h f d b 
'''
#Daily Workout log --> Fitness Streak
work_log = [1,1,1,0,1,1,0]
#Longest Streak
longest_streak = 0 #target
current_streak = 0 
#for including if,else
for day in work_log:
    #print(day)
    if day == 1: 
        current_streak+=1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(longest_streak)

        
        













































    






    









































































































