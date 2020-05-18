from playAudio import play_audio
from fuzzywuzzy import fuzz
from TextFromVoice import getVoiceFromText
from TextFromVoice import *
from TextFromVoice import record

import speech_recognition as sr
import os


opts = {"alias": ('nvoice', 'Нвойс', 'Энвойс'),
        "tbr": ('скажи', 'расскажи', 'покажи', 'сколько', 'произнеси', 'как','сколько','поставь','переведи', "засеки",'запусти','сколько будет'),
        "cmds":
            {"ctime": ('текущее время', 'сейчас времени', 'который час', 'время', 'какое сейчас время'),
             'startStopwatch': ('запусти секундомер', "включи секундомер", "засеки время"),
             'stopStopwatch': ('останови секундомер', "выключи секундомер", "останови"),
             "stupid1": ('расскажи анекдот', 'рассмеши меня', 'ты знаешь анекдоты', "шутка", "прикол"),
             "calc": ('прибавить','умножить','разделить','степень','вычесть','поделить','х','+','-','/'),
             "shutdown": ('выключи', 'выключить', 'отключение', 'отключи', 'выключи компьютер'),
             "conv": ("валюта", "конвертер","доллар",'руб','евро'),
             "internet": ("открой", "вк", "гугл", "сайт", 'вконтакте', "ютуб"),
             "translator": ("переводчик","translate"),
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
        pass
    elif cmd == 'shutdown':
        os.system('shutdown -s')
        getVoiceFromText("Выключаюсь...")
        play_audio()
    elif cmd == 'calc':
        pass
    elif cmd == 'conv':
        pass
    elif cmd == 'translator':
        pass
    elif cmd == 'stupid1':
        pass
    elif cmd == 'internet':
        pass
    elif cmd == 'startStopwatch':
        pass
    elif cmd == "stopStopwatch":
        pass
    elif cmd == 'deals':
        getVoiceFromText("У меня все хорошо")
        play_audio()
    else:
        print("Команда не распознана!")

def choice():
    #Выбор команды 
    if voice.startswith(opts["alias"]):
        cmd = voice

        for x in opts['alias']:
            cmd = cmd.replace(x, "").strip()

        for x in opts['tbr']:
            cmd = cmd.replace(x, "").strip()
        voice = cmd
        # распознаем и выполняем команду
        cmd = recognize_cmd(cmd)
        execute_cmd(cmd['cmd'])


record()