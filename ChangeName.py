import os
import os.path
import speech_recognition as sr
from pyglet import text
from playAudio import play_audio
from TextFromVoice import getVoiceFromText
from TheFirstSwitch import *
from SupportTFS import *

def ChangeName(r):
    os.remove('answer.txt')
    f = open('answer.txt', 'w')
    getVoiceFromText("Да, конечно. Произнесите мое новое имя")    
    play_audio()

    with sr.Microphone(device_index = index) as second:
        print("Говорите...")
        audio = r.listen(second)
    try:
        name = r.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + name)
        getVoiceFromText("Прекр+асно! Теперь мое второе имя " + name.lower() + ". Перезапуст+и+те колонку для применения изменений")
        play_audio()

        answer = name
        f.write(answer)
        f.close()
        return answer

    except sr.UnknownValueError:
        getVoiceFromText("Простите, я не рассл+ышала.")
        play_audio()
