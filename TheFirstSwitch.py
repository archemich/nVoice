import speech_recognition as sr
from pyglet import text
from playAudio import play_audio
from TextFromVoice import *

getVoiceFromText("Привет, меня зовут nVoice. Я Ваш новый голосовой ассистент. Желаете ли вы задать мне второе имя?")    
play_audio()

def zadanie(otvet):

    if 'нет' in otvet:
        getVoiceFromText("Хорошо, имя nVoice остается.")
        play_audio()  

    elif 'да' in otvet:
        getVoiceFromText("Произнесите н+овое имя.")
        play_audio()

        r = sr.Recognizer()
        with sr.Microphone(device_index=1) as second:
            print("Говорите...")
            r.adjust_for_ambient_noise(second, duration=1)
            source = r.listen(second)
        try:
            name = r.recognize_google(source, language="ru-RU").lower()
            print("Вы сказали: " + name)
            getVoiceFromText("Прекр+асно! Теперь мое второе имя " + name.lower())
            play_audio()
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio() 
            name = zadanie(otvet)   

        return name    
                  
while True:
     zadanie(RecordRecognizeVoice())