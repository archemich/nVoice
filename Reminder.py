import speech_recognition as sr
from pyglet import text
from playAudio import play_audio
from TextFromVoice import *
import time

def reminder(r):
    getVoiceFromText("С радостью Вам помогу. Что мне напомнить?")    
    play_audio()
    while True:
        with sr.Microphone(device_index = 1) as one:
            print("Говорите...")
            audio = r.listen(one)
        try:
            important_text = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + important_text)
            return important_text
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()

def chas(r):
    getVoiceFromText("Важно, произносите числа в именительном падеже. Через сколько часов Вам напомнить?")    
    play_audio()
    while True:
        with sr.Microphone(device_index = 1) as two:
            print("Говорите...")
            audio = r.listen(two)
        try:
            hour = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + hour)
            return hour
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()

def min(r):
    getVoiceFromText("Через сколько минут Вам напомнить?")    
    play_audio()
    while True:
        with sr.Microphone(device_index = 1) as three:
            print("Говорите...")
            audio = r.listen(three)
        try:
            minute = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + minute)
            return minute
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()

def sec(r):
    getVoiceFromText("Через сколько секунд Вам напомнить?")    
    play_audio()
    while True:
        with sr.Microphone(device_index = 1) as four:
            print("Говорите...")
            audio = r.listen(four)
        try:
            second = r.recognize_google(audio, language="ru-RU").lower()
            print("Вы сказали: " + second)
            return second
        except sr.UnknownValueError:
            getVoiceFromText("Простите, я не рассл+ышала.")
            play_audio()

def timecheck(important_text, hour, minute, second):
    hour = int(hour)
    minute = int(minute)
    second = int(second)
    local_time = hour * 3600 + minute * 60 + second

    time.sleep(local_time) 
    getVoiceFromText("Вы просили напомнить" + important_text)    
    play_audio()
    print('Вы просили напомнить:' + important_text)

    return local_time






    
