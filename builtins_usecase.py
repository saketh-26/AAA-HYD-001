'''
Use Random module --> Rock,paper,Scissors

import random
player1 = input('Enter the choice:-->Rock,Paper,Scissors:').lower()
player2 = random.choice(['Rock','Paper','Scissors']).lower()
print("Player2 Selection:",player2)
if player1 == "rock" and player2 == "paper":
    print("Player2 wins")
elif player1 == "paper" and player2 == "scissors":
    print("Player2 wins")
elif player1 == "scissors" and player2 == "rock":
    print("Player2 wins")
elif player1 == player2:
    print("Its a Tie")
else:
    print("Player1 wins")

#Task --> Build a Game Generator sequences -->Choice Menu
#1 - Rock Paper Scissors Game
#2 - Story Generator (random.choice()) [when,what,how,who,where --> lists]
#3 - OTP Generate to email
#4 - BMI Calculation
'''
#Build our own QR Code --> pyqrcode
#pip install pyqrcode
import pyqrcode,png
#take a link for which qrcode to be generated
link = "https://www.linkedin.com/in/saketh-codegnan/"
qr = pyqrcode.create(link)
print(qr)
qr.png("myqr.png",scale=15)
