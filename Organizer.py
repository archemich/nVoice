import time
import os
import TextFromVoice as tts
import playAudio

#Класс по работе с часами: Таймером, будильником и т.д
class Clock:

    #class Timer(<Минут до срабатывания таймера>)
    class Timer(object):
        def __init__(self, minutes):
            self.minutes = minutes
            secs = minutes * 60
            time.sleep(secs)
            playAudio.play_audio("alarm")

    #class Reminder(<количество минут до напоминания>, <текст, о котором напомнить>) 
    class Reminder (object):
        def __init__(self, minutes, text):
            self.minutes = minutes
            self.text = text
            time.sleep(2)
            playAudio.play_audio(tts.getVoiceFromText(text))