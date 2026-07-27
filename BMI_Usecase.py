'''
In this usecase (mini-project),we will make use of Control Block Statements 
#BMI --> Body Mass Index -->bmi = (weight (kg)) / (height**2) (metres)

desired_iteration = int(input("Enter the number of executions:"))
for i in range(desired_iteration):
    name = input("Enter the user name:")
    #weight = 70
    weight = int(input("Enter the weight in kgs:"))
    #height = 1.65
    height = float(input("Enter the height in metres:"))
    #print(bmi)
    #we want to make it dynamic  and build BMI Calculator
    #(<18.5 --> Underweight,18.5 - 24.9 -->Normal Weight,25 - 29.9 -->Overweight >=30 Obesity)
    if weight > 0 and height > 0:
        bmi = (weight) / ((height)**2)
        if bmi <18.5 :
            print(f'{name} --> You are Underweight as BMI is {bmi}')
        elif 18.5<=bmi<24.9:
            print(f'{name}-->You are in Perfect shape,BMi is {bmi}')
        elif 25<=bmi<29.9:
            print(f'{name}--> You are Overweight need to maintain diet,BMI is {bmi}')
        elif bmi>=30:
            print(f'{name} --> Obesity,your BMI is {bmi}')
    else:
        print(f'Enter only +ve values')

#Task --> For same above BMI Calculator store the details in a dictionary
#o/p as --> BMI_results = {'name':[user1,user2,user3],
#                           'BMI_Values':[bmi1,bmi2,bmi3]}
#user height -->inches,cms,feet -->metres

#Exception Handling -->try,except,finally

try:
    statement(s)...
    ......
except Errorname:
    debugging.........
finally:
    result.....
'''

while True: 
    try: 
        weight = int(input("Enter the weight in kgs.."))
        height = float(input("Enter the height in metres.."))
        if weight > 0 and height > 0:
            break
        else:
            print(f'Make sure to enter only +ve values,no Negative values..')
    except ValueError:
        print('Invalid input only integer for weight/int,float for height,enter properly')
    #except ZeroDivisionError:
        #print('Both zeros not allowed')
bmi = (weight) / ((height)**2)
if bmi <18.5 :
    print(f'You are Underweight as BMI is {bmi}')
elif 18.5<=bmi<24.9:
    print(f'You are in Perfect shape,BMi is {bmi}')
elif 25<=bmi<29.9:
    print(f'You are Overweight need to maintain diet,BMI is {bmi}')
elif bmi>=30:
        print(f'Obesity,your BMI is {bmi}')