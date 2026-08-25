#Now we will add subject and make sure to address is visible along with body
#of email using email package


import smtplib     #simple mail transfer protocol
#mime -->Multi Purpose Internet Mail Extension Protocol
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText

#defining data
From = "saketh@codegnan.com"  #give your email id
to = "saketh@codegnan.com"   #give receiver gmailid
subject = "Python testmail" #give your own subject
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = to
msg['Subject'] = subject
body = "Hello! first mail using python script" # The \n separates the message
msg.attach(MIMEText(body,'plain'))
text = msg.as_string()
#same usage of smtplib to start the process
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
#Next, log in to the server
server.login(From, "") #give your app passcode here 
#Send the mail
server.sendmail(From,to,text)
print("Mail Sent")
server.quit()



