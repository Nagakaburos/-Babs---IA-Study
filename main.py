#our main file.

import speech_recognition as sr

#criar um reconhecedor
r = sr.Recognizer()

#abrir o microfone para captura
with sr.Microphone() as source:
    while True:
        audio = r.listen(source) #Define microfone como entrada de audio.
    
        print(r.recognize_google(audio, language='pt'))
