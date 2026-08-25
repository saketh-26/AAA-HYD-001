#Input Formatting -->input()

#String input -->name,emailids,usernames...
#name = input() #here we will pass prompt
#print(name)
'''
name = input('Enter the username:')
print(name)
print(type(name))

#Integer input -->int() -->age,values,quantity
age = int(input("Enter the age:"))
print(age)
print(type(age))

#Float input -->discount,percentages...
discount = float(input("Enter the discounted value:"))
print(discount)
print(type(discount))

#costprice,selling price -->loss/profit
cost_price = int(input("enter the cost price"))
print(cost_price)
selling_price = float(input("Enter the SP"))
print(selling_price)
loss = cost_price - selling_price
print(loss)

#Multiple String inputs..
name,place = input("Enter the details:").split()
print(name)
print(place)
name,place = input("Enter the details:").split(',')
print(name)
print(place)

#Multiple integer values
a,b = map(int,input("Enter the values").split(','))
print(a)
print(b)

#Multiple float values
discount,weight = map(float,input("Enter the details:").split(','))
print(discount)
print(weight)

#List of strings
data = input("Enter the details:").split(',')
print(data)

#List of integers
marks = list(map(int,input("Enter the marks:").split(',')))
print(marks)

#List of float values
bmi_values = list(map(float,input("Enter the bmi:").split(',')))
print(bmi_values)
'''
#Output formatting
#print()
'''
print(25)
print(15,2.5,'codegnan')

#separator --> for separating the values
print(2026,7,9)
print(25,2.3,sep=',')
#above case we want as date format
print(2026,7,9,sep='-')
print(2026,7,9,sep='/')
print('codegnan','AAA',sep='<---------->')

#end argument in print() --> \n -->new line
name='codegnan'
place = 'hyderabad'
course ='AAA'
print(name,place)
print(course)
print(name,place,end=' ')
print(course)   
print(name,place,end='\t') #\t -->tab space
print(course)

#using commas
name = 'codegnan'
place = 'hyd'
print(name,place)
print("Name :",name,"Place :",place)
print("Name :",name,"Place :",place,sep=',')

#Old Style Formatting -->%d,%s,%f
age = 32;place = 'Hyd'
print("Age is %d and Place is %s"%(age,place))
price = 458.63
print("Item price is %f"%(price))
print("Item price is %.f"%(price))
print("Item price is %.1f"%(price))
print("Item price is %.2f"%(price))

#Using str().format() method
name,course = 'pavan','python'
print("{} is enrolled in {} course".format(name,course))
'''
#f-string Notation -->Most recommended
name,course = 'pavan','python'
print(f'{name} is enrolled in {course}')
print(f'{"Codegnan"}')
print('Codegnan')









































































































