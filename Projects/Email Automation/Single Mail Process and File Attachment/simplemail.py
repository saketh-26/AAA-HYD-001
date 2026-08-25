#Sending a simple email using Python
#smptlib -->simple mail transfer protocol
'''import smtplib
#connct to the server
server = smtplib.SMTP("smtp.gmail.com",587)
#start the server
server.starttls()
#login to the accnt
server.login("sakethreddy.kallepu@gmail.com","qswsnbzkypvfstda")#give your gmail app pwd
#enter your desired message
msg = "This is the First mail using Python"
#send the mail
server.sendmail("sakethreddy.kallepu@gmail.com","saketh@codegnan.com",
                msg)
'''
#Email OTP Authentication
import random
import math
import smtplib

#We will generatea 6 digit otp by taking base digits
digits = "0123456789"
OTP = "" #empty string

#now we will use math module along with module to generate a customized
#6 digit otp
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
    #print(OTP)
otp = OTP + " is your OTP"
msg= otp
#include our email automation 
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("saketh@codegnan.com", "") #app passcode
user="saketh@codegnan.com"
emailid = input("Enter the mail which you want to send OTP: ")
s.sendmail(user,emailid,msg)
a = input("Enter Your OTP >>: ")
if a == OTP:
    print("OTP Crrct")
else:
    print("Failure wrong OTP")












