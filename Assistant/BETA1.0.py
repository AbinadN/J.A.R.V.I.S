# IMPORTS
import os
import time
import pyaudio
import playsound
from gtts import gTTS
import openai
import speech_recognition as sr
import uuid

# API Key and Language Definition
api_key = 'key'
lang = 'en'
openai.api_key = api_key

# empty string to recognize the speaker
guy = ""

# infinite Loop to listen until STOP word said
while True:
    def get_adio():
# recognize speech from audio source
        r = sr.Recognizer()
        with sr.Microphone() as source:
# capture audio
            print("listening...")
            audio = r.listen(source)
            said = ""
# recognize speech and print
            try:
                said = r.recognize_google(audio)
                print(said)
                global guy
                guy = said
# if recognized extract JARVIS command and leave whitespace
                if "Jarvis" in said:
                    new_string = said.replace("Jarvis", "")
                    new_string = new_string.strip()
# forward command to GPT-3.5 and generate response
                    print("PROMPT:",new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                              messages=[{"role": "user", "content": new_string}])
                    text = completion.choices[0].message.content
# convert retrieved text to speech and plays audio response
                    speech = gTTS(text=text, lang=lang, slow=False, tld="co.uk")
                    file_name = f"welcome_{str(uuid.uuid4())}.mp3"
                    speech.save(file_name)
                    playsound.playsound(file_name, block=False)
# error occurring during speech recognition or response generation process
            except Exception as e:
                print(f"Speak Bitch! {str(e)}")
# returns the recognized speech
        return said
# recognizes STOP word
    if "hush" in guy:
        break
# initiate function
    get_adio()
