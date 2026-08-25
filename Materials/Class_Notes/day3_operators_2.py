#Membership Operators --> in,not in -->returns Boolean
#They check for the existance of an object in a collection
'''fruits = ['apple','orange','banana']
print('apple' in fruits)
print(45 in fruits)
print(45 not in fruits)
print(45 in [3,4,5,45])
print('5' in '231465')
print('code' in 'codegnan')

#Identity Operators --> id -->is,is not --> boolean value
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b)
print(a is b) #it returns False
print(id(a))
print(id(b))
c = a
print(c)
print(c is a)
print(c == a)
print(a is c)
print(id(a))
print(id(c))
print(c is not b)
#Logical Operators -->and,or,not -->boolean value

a = 14;b = 23
c = a < b and b > a
print(c)
d = a < b and 'code' in ['apple'] #it returns False as and need to have all conditions
#to be satisfied
print(d)
c = 12
#e = c+=5 #it raises an Error
#print(e)
e = b < c or a in [12,23,4,14]
print(e)
print(not(True))

#Bitwise Operators --> bitwise operations (binary)
#bitwise and,bitwise or,bitwise xor,shifting operators
#& , | , ^
print(5 & 2)
print(5 | 2)
print(5 ^ 8)

print(5 << 2)
print(5 >> 2)
'''
a = input("Enter a value")
b = int(input("Enter a value:"))
c = float(input("Enter a value:"))

print(a,b,c)














































