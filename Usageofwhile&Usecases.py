'''
Repetition Statements --> for,while

while --> checks until and unless the given condition is satisfied (True)

Syntax:

while condition:
    statement(s)..
    .....

#Simple usage to understand while
count = 0
while count < 5:
    print("okay you have access")
    a = []
    a.append("codegnan")
    print(a)
    count = count+1 #Addition Assignment operator
  
#Checking the valid attempts -->Counter 
count = 5
while count >= 1:
    print(f'Count = {count}')
    count= count - 1

#To find a valid password
password = input("Enter the password:")
while password != "admin":
    print(f'Incorrect password')
    password = input("Enter the correct password")
print(f'Hurray its done-->Access granted')

#Now give only 3 chances for password check -->if more than 3 print Account Locked.
chance = 1
password = input("Enter the password:")
while password != 'admin':
    print(f'Incorrect password')
    if chance >= 3:
        print("Account is Freezed")
        break
    chance = chance + 1
    password = input("Enter the password")
else:
    print("Login Successful")

#for with else,while with else --->else will be executed only when loop is completely done
#Search for a product in the store

search = input("Enter the search item:").lower()
store = ["mobile","laptop","powerbank","charger"]
for item in store:
    if search == item:
        print(f'Item is found')
        break
else:
    print(f'Item is missing')

#task : PIN Verification user should be given 3 chances if 3rd chance is over
#it should return Account locked for 24hours -->balance withdrawl,show the number of chanc es
    
#Push it to Github and linkedin post

#break,continue,pass -->Jumping statements
#break -->it terminates the loop once the given condition is satisfied

#continue --> it basically skips the current iteration and gets back to the next iteration..

for i in "codegnan":
    if i == "g":
        continue
        #break
    print(i)
'''
#pass -->It is generally used as a placeholder (to have any syntax matches)

for i in range(10):
    pass
    #print("hello")


    







    








        
        
        








    
    
 








    
    









