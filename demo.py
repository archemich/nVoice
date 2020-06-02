from playAudio import play_audio
from fuzzywuzzy import fuzz
from TextFromVoice import getVoiceFromText
from TimeChecker import localtime
from CheckCharge import accurate_charge_percent
from TheFirstSwitch import *
from SupportTFS import *
from Sensors import * 
from Weather import get_city
import requests
import json


import speech_recognition as sr
import os
import time

personal_name = new_name()

r = sr.Recognizer()
m = sr.Microphone(device_index=0)

google_access_token = 'AIzaSyDn9D53ztPOLR5bGyQdjkxpRR3PCkNVJ5c'
 
def RecognizeSpeech():
    voice = ''
    with m as f:
        print("Говорите...")
        audio = r.adjust_for_ambient_noise(f)
        audio = r.listen(f)
        try:
            voice = r.recognize_google(audio, google_access_token, "ru-RU").lower()
            
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        
    return voice
    

#Распознавание голоса
def recognize(voice):
    try:
        for _ in opts["alias"]:
            if _ in voice:
                cmd = voice

                for x in opts['alias']:
                    cmd = cmd.replace(x, "").strip()

                for x in opts['tbr']:
                    cmd = cmd.replace(x, "").strip()

                voice = cmd
                cmd = recognize_cmd(cmd)
                execute_cmd(cmd['cmd'], voice)
                break

    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        getVoiceFromText("Неизвестная ошибка, проверьте интернет!")
        play_audio()


opts = {"alias": ('nvoice', 'нвойс', 'энвойс', 'инвойс', 'voice', 'войс', 'нвс', 'энн воис', 'нваэс', 'н вайс', personal_name),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как', 'сколько', 'какая', 'насколько'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             "charge": ('заряда','процентов','ты заряжен','ты разряжен'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи'),
             "deals": ('дела','делишки', 'сам', 'у тебя дела'),
             "temperature": ('температура в комнате', 'градусов в комнате', 'температур'),
             "humudity": ('влажность', 'влажн'),
             "co2": ('цо2', 'co2', 'углекислый газ', 'газ'),
             "commonCond": ('состояние помещения', 'состояние', 'состояние комнаты'),
             "weather": ('погода в', 'погода')
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
        #os.system('shutdown -s')
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
    


if __name__ == "__main__":
    while True:
        text = RecognizeSpeech()
        print("\nYou said: {}".format(text))
        recognize(text)