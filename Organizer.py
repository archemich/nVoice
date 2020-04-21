import time
import os
import TextFromVoice as tts

#Класс по работе с часами: Таймером, будильником и т.д
class Clock:

    #class Timer(<Минут до срабатывания таймера>)
    class Timer(object):
        def __init__(self, minutes):
            self.minutes = minutes
            secs = minutes * 60
            time.sleep(secs)
            os.startfile(os.path.dirname(__file__) + "/audio/alarm.wav")

    #class Reminder(<количество минут до напоминания>, <текст, о котором напомнить>) 
    class Reminder (object):
        def __init__(self, minutes, text):
            self.minutes = minutes
            self.text = text
            Clock.Timer(minutes)
            time.sleep(2)
            tts.getVoiceFromText(text)
            os.startfile(os.path.dirname(__file__) + "/audio/AudioResult.wav")