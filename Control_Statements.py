#print(2+3)
'''
assert -> assert keyword is mainly used for debugging cases in development,it checks for the given conditon to be validated
whereas if condition is False it raises AssertionError
Syntax:
assert condition,"Error message" #Error message is userdefined

x = int(input("Enter a positive number:"))
#assert x > 0 
#assert x>0,"Value should be only +ve"
#x = x+2
#print(f'Updated value is {x}')
assert x in [12,23,45],"checking data"
print(f'Search Found')

#Nested Loops --> A loop placed inside another loop --> Pattern Generations..
Syntax:
for i in range(outer_loop):
    for j in range(inner_loop):
        #statement(s)... for every outer loop inner loop will be completely executed
        ...... outer loop -->rows ,inner loop -->columns

for i in range(3):#i -->0,1,2
    for j in range(2): #j-->0,1
        #print(f'Value of i is {i},Value of j is {j}')
        print(i,j)
for i in range(2):
    for j in range(4):
        print(i,j)'''
#Number patterns,Row based number patterns,COlumn based number patterns,traingle...
'''
1 2 3
1 2 3
1 2 3

for i in range(1,4):
    for j in range(1,4):
        print(j,end=' ')
print()

1 1 1
2 2 2
3 3 3
for i in range(1,4):
    for j in range(1,4):
        print(i,end=' ')
    print()
A A A
B B B
C C C
#you can use ord()

for i in range(65,68):
    for j in range(1,4):
        print(chr(i),end=' ')
    print()
1 2 3
4 5 6
7 8 9

num = 1
for i in range(1,4):
    for j in range(1,4):
        #i = i+1
        print(num,end=' ')
        num=num+1
        #print(i,j)
    print()
Square Pattern
* * *
* * *
* * *

for i in range(3):
    for j in range(3):
        print('*',end=' ')
    print()
#Solid Rectangle 
* * * *
* * * * 
* * * *

for i in range(3):
    for j in range(4):
        print('*',end=' ')
    print()

*
* *
* * *
* * * *

#let's assume we want to have 4 rows
n = 4
for i in range(1,n+1):
    for j in range(i):
        #print(f'Value of i is {i},Value of j is {j}')
        print('*',end=' ')
    print()
#Home Tasks
#Inverted triangle 
* * * *
* * *
* *
*

#Flyods Triangle
1
2 3
4 5 6
7 8 9 10

\
A
B C
D E F
G H I J
'''

