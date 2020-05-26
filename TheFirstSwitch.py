import speech_recognition as sr
from pyglet import text
from playAudio import play_audio
from TextFromVoice import *

google_access_token = 'AIzaSyDn9D53ztPOLR5bGyQdjkxpRR3PCkNVJ5c'

def command():
    getVoiceFromText("Привет, меня зовут nVoice. Я Ваш новый голосовой ассистент. Желаете ли вы задать мне второе имя?")    
    play_audio()
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=1) as first:
            print("Говорите...")
            r.adjust_for_ambient_noise(first, duration=0)
            audio = r.listen(first)
        try:
            otvet = r.recognize_google(audio, google_access_token, language="ru-RU").lower()
            print("Вы сказали: " + otvet)
            return otvet
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()

def zadanie(otvet):

    name = 'nvoice'
    if 'нет' in otvet:
        getVoiceFromText("Хорошо, имя nVoice остается.")
        play_audio()  

    elif 'да' in otvet:
        getVoiceFromText("Произнесите н+овое имя.")
        play_audio()

        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as second:
            print("Говорите...")
            r.adjust_for_ambient_noise(second, duration=0)
            source = r.listen(second)
        try:
            name = r.recognize_google(source, language="ru-RU").lower()
            print("Вы сказали: " + name)
            getVoiceFromText("Прекр+асно! Теперь мое второе имя " + name.lower())
            play_audio()
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()    
    else:
        getVoiceFromText("В вашем ответе не прозвучало да или нет. Имя останется прежним.")
        play_audio()

    return name    