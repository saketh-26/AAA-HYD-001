'''
Nested Conditions -->One condition inside another --> if,else

Syntax :

if condition :
    if condition2:
        statement(s)...
        ....
    elif condition3..:
        statement(s)....
        .....
    ......
else:
    statement(s)....
    .....
'''

#Usecase : ATM Withdrawl scenario
#Check whether card is valid/not -->entered pin is correct or not -->chck balance
#-->withdrawl

card_inserted = True
correct_pin = True
balance = 10000
with_drawl_amount = int(input("Enter the amount to withdraw:"))
if card_inserted:
    if correct_pin:
        if balance > with_drawl_amount:
            print(f'Transaction is Successful,New balance is {balance - with_drawl_amount}')
        else:
            print(f'Transacation Failed,please maintain sufficient balance')
    else:
        print(f'Wrong PIN entered')

else:
    print(f'Your Card is Not in Use')

#You try out your scenario... -->saketh@codegnan.com 
























