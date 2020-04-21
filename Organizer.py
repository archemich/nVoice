import time
import os
import TextFromVoice as tts

#Класс по работе с часами: Таймером, будильником и т.д
class Clock:

    #Класс таймера. На вход получает одно значение - количество минут до срабатывания таймера.
    class Timer(object):
        def __init__(self,minutes):
            self.minutes = minutes
            secs = minutes * 60
            time.sleep(secs)
            os.startfile(os.path.dirname(__file__) + "/audio/alarm.wav")

    #Класс напоминалки. На вход получает время в минутах до срабатывания таймера и текст, о котором напоминает 
    class Reminder (object):
        def __init__(self,minutes,text):
            self.minutes = minutes
            self.text = text
            Clock.Timer(minutes)
            tts.getVoiceFromText(text)
            time.sleep(1)
            os.startfile(os.path.dirname(__file__) + "/audio/AudioResult.wav")