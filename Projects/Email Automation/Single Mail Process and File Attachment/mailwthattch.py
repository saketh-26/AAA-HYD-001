import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os #to read files from your local system

From = "" #enter your gmail username
app_passcode = "" #enter your gmail app passcode
to = '' #enter to whom you want to send
subject = "Mail with attachment"
text = "Sample test mail for attachment sending" #body of mail
attach = 'simplemail.py' #give your attachment name
msg = MIMEMultipart()
msg['From'] = From
msg['To'] = to
msg['Subject'] = subject
msg.attach(MIMEText(text))
#To load and encode the attachement
part = MIMEBase('application', 'octet-stream')
part.set_payload(open(attach, 'rb').read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',
   'attachment; filename="%s"' % os.path.basename(attach))
msg.attach(part)
#Server connection starts..
mailserver = smtplib.SMTP("smtp.gmail.com",587)
mailserver.starttls()
mailserver.login(From, app_passcode)
mailserver.sendmail(From, to, msg.as_string())
print("Done")
#close the connection
mailserver.close()
