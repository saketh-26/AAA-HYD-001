#Now in this case we will use email package where we can add subject to the mail and also 
#we can give to address..
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
'''#give from address,to address and subject 
From = "saketh@codegnan.com"
To = "vasanthikalavakuri@gmail.com"
Subject = "Agentic AI Classes"
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
body = "Hope you are following Python classes,make sure to practice more.."
msg.attach(MIMEText(body))
#entire message to string format
text = msg.as_string()
#same as previous SMTP usage we will follow
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('saketh@codegnan.com','srrp debj auub eisn')
server.sendmail(From,To,text)
print("Mail Sent")
server.quit()

#Send an OTP to user and validate it 
import math,random
From = "saketh@codegnan.com"
To = "vasanthikalavakuri@gmail.com"
Subject = "Agentic AI Classes"
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
#will give base digits
digits = '0123456789'
OTP=""
for i in range(6):
    OTP+= digits[math.floor(random.random()*10)]
    #print(OTP)
body = 'Your OTP is'+OTP
msg.attach(MIMEText(body))
#entire message to string format
text = msg.as_string()
#same as previous SMTP usage we will follow
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('saketh@codegnan.com','srrp debj auub eisn')
server.sendmail(From,To,text)
print("Mail Sent")
a = input("Enter the OTP received")
if a == OTP:
    print(f'Login Success')
else:
    print(f'Login Failure')
'''