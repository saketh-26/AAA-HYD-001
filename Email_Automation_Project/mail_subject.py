'''
We want to send Automated Email using Python by adding attachment (file)
'''
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
#same include mailwith subject code
From = "saketh@codegnan.com"
To = "vasanthikalavakuri@gmail.com"
Subject = "Email Automation using Python - Single User with Attachment"
app_password = "srrp debj auub eisn"
body = "In this project we will understand how Python can be useful in real world applications"
attach = "simplemail.py" #give your attachment name
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = To
msg['Subject'] = Subject
msg.attach(MIMEText(body))
#now we need to add file attachment 
part = MIMEBase('application','octet-stream')
part.set_payload(open(attach,'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Dispostion','attachment ;filename="%s" ' %(os.path.basename(attach)))
msg.attach(part)
text=msg.as_string(part)
#start the server communication
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(From,app_password)
server.sendmail(From,To,text)
print("Mail Sent")
server.quit()





