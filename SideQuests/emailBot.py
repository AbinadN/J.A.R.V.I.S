# Programming Hero Inspo

import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:

        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()

    except:
        pass

# Manually Added Contact List
email_list = {
    'dude': 'jhankar@gmail.com',
    'dad': 'nagatheeban@gmail.com',
    'mom' : 'umaiyal2000@yahoo.com',


}

def send_email(receiver,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('abinad.naga@gmail.com', '')
    email = EmailMessage()
    email['From'] = 'abinad.naga@gamil.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

    talk("It's sent!")
    talk("Would you like to send another?")
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()

def get_email_info():
    talk('To whom, would you like to send the email?')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('What would you like to write to them?')
    message = get_info()

    send_email(receiver,subject,message)


get_email_info()

