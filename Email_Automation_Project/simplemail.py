'''
Step1: --> Setting up Gmail App Password  (2 Step Verification ON)
We will use SMTP (Simple Mail Transfer Protocol) 
#Step2: using SMTPLIB we start the communication
'''
import smtplib
#first we will make the protocol connection
server = smtplib.SMTP('smtp.gmail.com',587)
print(server)
#Start communication
server.starttls()
#we will make the login
server.login('saketh@codegnan.com','srrp debj auub eisn')
print("Login Success")
message = "Welcome to my World..This is an Automated Mail..."
#Send the mail
server.sendmail('saketh@codegnan.com','abhiramdumpala2004@gmail.com',message)
print("Success")