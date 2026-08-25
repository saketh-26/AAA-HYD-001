#Building Virtual Assistant to perform customized tasks

from gtts import gTTS
import speech_recognition as sr
import playsound
import uuid
import os
from time import ctime
import webbrowser
import re #regular expressions to find/search patterns


#define a function to recognize our voice
#First let's make our voice to be recognized
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Start talking now...") #own statement
        audio = r.listen(source,phrase_time_limit=5)
    data = ""
    #Exception Handling
    try:
        data = r.recognize_google(audio,language='en-US')
        print("You said:"+data)
    except sr.UnknownValueError:
        print("I cannot hear you speak louder")
    except sr.RequestError as e:
        print("Request Failed")
    return data
    #tts = gTTS(text = data,lang='en', tld='co.in')
    #tts.save("speech.mp3")
    #playsound.playsound("speech.mp3")
#listen()

#now let's make it to respond back
def respond(String):
    print(String)
    tts = gTTS(text = String,lang='en', tld='co.in')
    tts.save("speech.mp3")
    filename = "Speech%s.mp3"%str(uuid.uuid4())
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

#We will start giving actions for it
def virtual_asstnt(data):
    """give your actions"""
    if "how are you" in data:
        listening = True
        respond("Good and doing well")
    elif "time" in data:
        listening = True
        respond(ctime())
    elif "open google" in data.casefold(): #lowercase conversion
        listening = True
        reg_ex = re.search('open google(.*)',data)
        url = "https://www.google.com/"
        if reg_ex:
            sub = reg_ex.group(1)
            url = url + 'r/' #rawstrings to map even slashes also as characters
        webbrowser.open(url)
        respond("Success")
    elif "locate" in data.casefold():
        listening = True
        webbrowser.open('https://www.google.com/maps/search/'+
                        data.replace("locate",""))
        result = "Located"
        respond("Located {}".format(data.replace("locate","")))
    elif "email" in data:
        listening = True
        respond("Whom should i send email to?")
        to = listen()
        edict = {'hello':'saketh@codegnan.com','new':''} #give mail ids
        toaddr = edict[to]
        respond("What is the Subject?")
        subject = listen()
        respond("What should i tell that person?")
        message = listen()
        content = 'Subject :{}\n\n{}'.format(subject,message)

        #init gmail SMTP
        mail = smtplib.SMTP('smtp.gmail.com',587)
        #identify the server
        mail.ehlo()
        mail.starttls()
        #login
        mail.login('','') #enter mailid and app password make sure you enable less secure app access
        mail.sendmail('',toaddr,content) #enter your gmail username
        mail.close()
        respond('Email Sent')
    
    elif "stop talking" in data:
        listening = False
        respond("Okay done take care")
    try:
        return listening
    except UnboundLocalError:
        print("Timedout")
        
respond("Hey Codegnan how are you") #frst greeting from vrtualassnt
listening = True
while listening == True:
    data = listen()
    listening = virtual_asstnt(data)






