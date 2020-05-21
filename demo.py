from playAudio import play_audio
from fuzzywuzzy import fuzz
from TextFromVoice import getVoiceFromText
from TimeChecker import localtime
from CheckCharge import accurate_charge_percent
from TheFirstSwitch import *

import speech_recognition as sr
import os
import time

personal_name = zadanie(command()).lower()

r = sr.Recognizer()
m = sr.Microphone(device_index=0)

voice = 'str'

#Распознавание голоса
def recognize(voice):
    try:
        print("Распознано: " + voice)
        for _ in opts["alias"]:
            if _ in voice:
                cmd = voice

                for x in opts['alias']:
                    cmd = cmd.replace(x, "").strip()

                for x in opts['tbr']:
                    cmd = cmd.replace(x, "").strip()

                voice = cmd
                # распознаем и выполняем команду
                cmd = recognize_cmd(cmd)
                execute_cmd(cmd['cmd'])
                break

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        getVoiceFromText("Неизвестная ошибка, проверьте интернет!")
        play_audio()

    

#Запись голоса
def record():
    with sr.Microphone(device_index=1) as first:
        print("Говорите...")
        r.adjust_for_ambient_noise(first, duration=0)
        audio = r.listen(first)
        try:
            otvet = r.recognize_google(audio, language="ru-RU").lower()
            recognize(otvet)
            
        except sr.UnknownValueError:
            pass

opts = {"alias": ('nvoice', 'нвойс', 'энвойс', 'инвойс', 'voice', 'войс', 'in ice', 'on ice', 'нвс', 'android', 'конвой', 'он возит', personal_name),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как','сколько','поставь','переведи', "засеки",'запусти','сколько будет', 'насколько'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             "charge": ('заряда','процентов','ты заряжен','ты разряжен'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи'),
             "deals": ("дела","делишки", 'как сам', 'как дела')}}

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    return RC

def execute_cmd(cmd):
    if cmd == 'ctime':
        localtime()
    elif cmd == 'shutdown':
        os.system('shutdown -s')
        getVoiceFromText("Выключаюсь...")
        play_audio()
    elif cmd == 'charge':
        accurate_charge_percent()
    elif cmd == 'deals':
        getVoiceFromText("У меня все хорошо")
        play_audio()
    else:
        print("Команда не распознана!") 

while True:
    record()