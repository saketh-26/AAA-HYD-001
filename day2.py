#basic Decision Making

#Number Classification System (Positive / Negative / Zero)
#if,elif,else
#Accept input from user
'''
num = int(input("Enter the value:"))
#print(num)
if num > 0:
    print(f'Num is Positive and it is {num}')
elif num < 0:
    print(f'Num is Negative and it is {num}')
else:
    print("Zero")
'''

#Comparision Chaining

#Instead of writing as if x > 0 and x < 100
#can also be written as if 0 < x < 100
#variable should be in between only

#Basic Range check
'''
num = int(input())
if 0<num<100: #if x > 0 and x < 100
    print("x is between values of 0 to 99")
else:
    print("x is out of range")
'''
#Multi Conditional Logic -->Grade System
#Highest marks --> >=90 -->'A'
#--> >= 75 -> 'B'
#-->>=50 -->'C'
#-->Fail
'''
#marks to be in range of 0-100
marks = int(input("Enter the value:"))

if marks > 0 or marks <100:
    print("Only Enter value in between 0-100")
#if marks >= 90:
    #print(f'Grade is A')
elif marks >= 75:
    print(f'Grade is B')
elif marks >=50:
    print(f'Grade is C')
else:
    print(f'Failed Student,prepare well...')

#Largest of 3 numbers

a,b,c = map(int,input("Enter 3 values:").split())
#print(a,b,c)
if a >=b and a >=c:
    print(f"Value of a is greater and it is {a}")
elif b >=a and b >=c :
    print(f"Value of b is greater and it is {b}")
else:
    print(f"Value of c is greater and it is {c}")
'''

#Task: Build a Billing Discount System with the below possibilities
#amount greater than 1000 --> 20%
#amount greater than 500 -->10%
#less than 500 no discount
#then print the final amount
#Post screenshots in whatsapp group

name,*line = input().split()
print(name)
print(line)


































