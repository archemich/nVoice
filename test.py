import speech_recognition as sr
from pyglet import text
from playAudio import play_audio
from TextFromVoice import *
import time
from Reminder import *

r=sr.Recognizer()
reminder(r)
chas(r)
min(r)
sec(r)
timecheck(reminder(r), chas(r), min(r), sec(r)).lower()   

