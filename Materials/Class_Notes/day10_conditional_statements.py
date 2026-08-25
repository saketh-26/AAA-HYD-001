'''
Control Statements -->These are the statements which control the flow of execution of
the program

-->Conditional Statements (if,else,elif)-->Nested if statements
-->Repetition Statements (Loops) --> for,while ,Nested loops (Patterns)
-->Jumping Statements --> break,continue,pass,assert
'''

#if statement:
'''

if <condition>:
    statement(s)...
    .......
    ....

#validate the price..
#money = 100   
money = int(input("Enter the  billing value:")) #dynamic input
if money <= 100:
    print(f'Now you are eligible to get your items')
print("Check again")

students = ['ram','akash','abhi','mani']
name = input("Enter the student name:").lower()
if name in students:
    marks = 50
    grade = 'A'
    print(f'{name} has secured {marks} marks and {grade} Grade')

if-else statements...

Syntax:

if condition:
    statement(s)
    .....
    ...
else:
    statement(s)...
    .....

#Vote Eligibility...
#User will enter his/her age --> give voter eligibility
age = int(input("Enter the age:"))
if age>=18:
    print(f'You are eligible to vote,so use it properly')
    print("Your age is {} years,eligible".format(age))
else:
    print("You are not eligible to vote")
    print(f'You need to wait for {18-age} years to get vote right')

if-elif-else statement(s)....
....

syntax:

if condition1:
    statemnt(s)...
    .....
elif condition2:
     statmnt(s)...
     .....
     ....
elif condition(3):
    ....
    ...
else:
    statement(s)...
    ....
'''
#For same above Vote Elibility we rewrite the logic
age = int(input("Enter the age:"))
if age>=18:
    print(f'You are eligible to vote,so use it properly')
    print("Your age is {} years,eligible".format(age))
elif age==0 or age < 0:
    print(f'Enter only +ve values')
else:
    print("You are not eligible to vote")
    print(f'You need to wait for {18-age} years to get vote right')









































    



































