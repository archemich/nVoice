import speech_recognition as sr
from pyglet import text
from playAudio import play_audio
from TextFromVoice import *

index = 0

def command():
    getVoiceFromText("Привет, меня зовут nVoice. Я Ваш новый голосовой ассистент. Желаете ли вы задать мне второе имя?")    
    play_audio()
    r = sr.Recognizer()
    while True:
        with sr.Microphone(device_index = index) as first:
            print("Говорите...")
            audio = r.adjust_for_ambient_noise(first)
            audio = r.listen(first)
        try:
            otvet = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + otvet)
            return otvet
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()

def zadanie(otvet):
    f = open('answer.txt', 'w')

    name = 'nvoice'
    if 'нет' in otvet:
        answer = 'nvoice'
        f.write(answer)
        f.close()

        getVoiceFromText("Хорошо, имя nVoice остается.")
        play_audio()  

    elif 'да' in otvet:
        getVoiceFromText("Произнесите н+овое имя.")
        play_audio()
        r = sr.Recognizer()
        with sr.Microphone(device_index = index) as second:
            print("Говорите...")
            audio = r.adjust_for_ambient_noise(second)
            audio = r.listen(second)
        try:
            name = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + name)
            getVoiceFromText("Прекр+асно! Теперь мое второе имя " + name.lower())
            play_audio()

            answer = name
            f.write(answer)
            f.close()

        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()    
    else:
        getVoiceFromText("В вашем ответе не прозвучало да или нет. Имя останется прежним.")
        play_audio()
        
        f = open('answer.txt', 'w')
        answer = 'nvoice'
        f.write(answer)
        f.close()

    return name  

     