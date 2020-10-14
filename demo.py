from playAudio import play_audio
from fuzzywuzzy import fuzz
from TextFromVoice import getVoiceFromText
from TimeChecker import localtime
from CheckCharge import accurate_charge_percentfrom playAudio import play_audio
from fuzzywuzzy import fuzz
from TextFromVoice import getVoiceFromText
from TimeChecker import localtime
from CheckCharge import accurate_charge_percent
from TheFirstSwitch import *
from SupportTFS import *
from Sensors import * 
from ChangeName import *
from Weather import get_city
#from Reminder import Timer
from Reminder import Timer
from VoiceControl import setVolume
import requests
import json
import wikipedia

import speech_recognition as sr
import os
import time

index = 0

r = sr.Recognizer()
m = sr.Microphone(device_index=index)

##############################################################
getVoiceFromText("Пару секунд тишины пожалуйста. Калибровка.")
play_audio()
print("сек")
with m as source:
    r.adjust_for_ambient_noise(source)
print("говор")
##############################################################
personal_name = new_name(r, index)

wikipedia.set_lang("RU")

def activate():
    try:
        with m as source:
            audio = r.listen(source)
            transcript = r.recognize_google(audio, language="ru-RU").lower()
            print(transcript)
            if (transcript.lower()).startswith(opts['alias']):
                return True
            else:
                return False
    except:
        return False

def RecognizeSpeech():
    if True:
        voice = ''
        with m as f:
            print("Говорите...")
            getVoiceFromText("pip")
            play_audio()
            audio = r.listen(f)
            try:
                voice = r.recognize_google(audio, language="ru_RU").lower()
                print(voice)
                recognize(voice)
            except sr.UnknownValueError:
                print("[GoogleSR] Неизвестное выражение")
            except sr.RequestError as e:
                print("[GoogleSR] Не могу получить данные; {0}".format(e))

#Распознавание голоса
def recognize(voice):
    try:
        cmd = voice

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()

        voice = cmd
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'], voice)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        getVoiceFromText("Неизвестная ошибка, проверьте интернет!")
        play_audio()
        pass


opts = {"alias": ('nvoice', 'нвойс', 'энвойс', 'инвойс', 'voice', 'войс', 'нвс', 'энн воис', 'нваэс', 'н вайс', personal_name),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'сколько', 'какая', 'насколько', 'давай сменим', 'поменяй', 'измени', 'напомни', 'какое','что','кто'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             "charge": ('заряда','процентов','ты заряжен','ты разряжен'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи'),
             "deals": ('дела','делишки', 'сам', 'у тебя дела'),
             "temperature": ('температура в комнате', 'градусов в комнате', 'температур'),
             "humudity": ('влажность', 'влажн'),
             "co2": ('цо2', 'co2', 'углекислый газ', 'газ'),
             "commonCond": ('состояние помещения', 'состояние', 'состояние комнаты'),
             "weather": ('погода в', 'погода'),
             "changename": ('имя', 'название'),
             "remindMe": ('мне'),
	         "wiki":('такое','такая','такой'),
             "setVolume": ('громкость')
             }}

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    if(RC['percent'] >= 50):
        return RC
    else:
        print("Команда не распознана!") 
        return {'cmd': 'none'}

def execute_cmd(cmd, voice):
    if cmd == 'ctime' :
        localtime()
    elif cmd == 'shutdown':
        os.system('sudo shutdown -h now')
        getVoiceFromText("Выключаюсь...")
        play_audio()
    elif cmd == 'charge':
        accurate_charge_percent()
    elif cmd == 'deals':
        getVoiceFromText("У меня все хорошо")
        play_audio()
    elif cmd == 'temperature':
        sensor_temp_status()
    elif cmd == 'humudity':
        sensor_humidity_status()
    elif cmd == 'co2':
        sensor_CO2_status()
    elif cmd == 'commonCond':
        all_sensors_status()
    elif cmd == 'weather':
        get_city(voice)
    elif cmd == 'changename':
        personal_name = ChangeName(r, index)
        print(personal_name)
    elif cmd == 'wiki':
	    GetVoiceFromText(wikipedia.summary(voice))
	    play_audio()
    elif cmd == 'setVolume':
	    setVolume(voice)
    #elif cmd == 'remindMe':
	    #Timer(voice)


    getVoiceFromText('pibip')
    play_audio()

if __name__ == "__main__":
    while True:
        RecognizeSpeech()

from TheFirstSwitch import *
from SupportTFS import *
from Sensors import * 
from ChangeName import *
from Weather import get_city
#from Reminder import Timer
from Reminder import Timer
from VoiceControl import setVolume
import requests
import json
import wikipedia

import speech_recognition as sr
import os
import time

index = 0

r = sr.Recognizer()
m = sr.Microphone(device_index=index)

##############################################################
getVoiceFromText("Пару секунд тишины пожалуйста. Калибровка.")
play_audio()
print("сек")
with m as source:
    r.adjust_for_ambient_noise(source)
print("говор")
##############################################################
personal_name = new_name(r, index)

wikipedia.set_lang("RU")

def activate():
    try:
        with m as source:
            audio = r.listen(source)
            transcript = r.recognize_google(audio, language="ru-RU").lower()
            print(transcript)
            if (transcript.lower()).startswith(opts['alias']):
                return True
            else:
                return False
    except:
        return False

def RecognizeSpeech():
    if True:
        voice = ''
        with m as f:
            print("Говорите...")
            getVoiceFromText("pip")
            play_audio()
            audio = r.listen(f)
            try:
                voice = r.recognize_google(audio, language="ru_RU").lower()
                print(voice)
                recognize(voice)
            except sr.UnknownValueError:
                print("[GoogleSR] Неизвестное выражение")
            except sr.RequestError as e:
                print("[GoogleSR] Не могу получить данные; {0}".format(e))

#Распознавание голоса
def recognize(voice):
    try:
        cmd = voice

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()

        voice = cmd
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'], voice)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        getVoiceFromText("Неизвестная ошибка, проверьте интернет!")
        play_audio()
        pass


opts = {"alias": ('nvoice', 'нвойс', 'энвойс', 'инвойс', 'voice', 'войс', 'нвс', 'энн воис', 'нваэс', 'н вайс', personal_name),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'сколько', 'какая', 'насколько', 'давай сменим', 'поменяй', 'измени', 'напомни', 'какое','что','кто'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             "charge": ('заряда','процентов','ты заряжен','ты разряжен'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи'),
             "deals": ('дела','делишки', 'сам', 'у тебя дела'),
             "temperature": ('температура в комнате', 'градусов в комнате', 'температур'),
             "humudity": ('влажность', 'влажн'),
             "co2": ('цо2', 'co2', 'углекислый газ', 'газ'),
             "commonCond": ('состояние помещения', 'состояние', 'состояние комнаты'),
             "weather": ('погода в', 'погода'),
             "changename": ('имя', 'название'),
             "remindMe": ('мне'),
	     "wiki":('такое','такая','такой'),
             "setVolume": ('громкость')
             }}

def recognize_cmd(cmd):
    RC = {'cmd': '', 'percent': 0}
    for c, v in opts['cmds'].items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > RC['percent']:
                RC['cmd'] = c
                RC['percent'] = vrt
    if(RC['percent'] >= 50):
        return RC
    else:
        print("Команда не распознана!") 
        return {'cmd': 'none'}

def execute_cmd(cmd, voice):
    if cmd == 'ctime' :
        localtime()
    elif cmd == 'shutdown':
        os.system('sudo shutdown -h now')
        getVoiceFromText("Выключаюсь...")
        play_audio()
    elif cmd == 'charge':
        accurate_charge_percent()
    elif cmd == 'deals':
        getVoiceFromText("У меня все хорошо")
        play_audio()
    elif cmd == 'temperature':
        sensor_temp_status()
    elif cmd == 'humudity':
        sensor_humidity_status()
    elif cmd == 'co2':
        sensor_CO2_status()
    elif cmd == 'commonCond':
        all_sensors_status()
    elif cmd == 'weather':
        get_city(voice)
    elif cmd == 'changename':
        personal_name = ChangeName(r, index)
        print(personal_name)
    elif cmd == 'wiki':
	GetVoiceFromText(wikipedia.summary(voice,sentences=2))
	play_audio()
    elif cmd == 'remindMe':
	Timer(voice)
    elif cmd == 'setVolume':
	setVolume(voice)


    getVoiceFromText('pibip')

if __name__ == "__main__":
    while True:
        RecognizeSpeech()
