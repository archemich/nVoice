from functools import partial
from alsaaudio import Mixer
from playAudio import play_audio
from TextFromVoice import getVoiceFromText
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
vol = 70
VOLSTEP = 5

def setVolume(text):
    text = ''.join(text).split()
    volume = int(text[text.index('на') + 1])
    global vol
    vol = volume
    print(text)
    print(volume)
    if volume >= 0 and volume <= 100:
        mix = Mixer()
        mix.setvolume(volume)
        print("Громкость =", str(volume))
    else:
        getVoiceFromText("Нельзя поставить громкость на", (str(volume)))
        print("Нельзя поставить громкость на", (str(volume)))
       
def changeVolume(volume):
    global vol
    if volume >= 0 and volume <= 100:
        mix = Mixer()
        mix.setvolume(volume)
        vol = volume
        print("Громкость =", vol)
    
    
    
BUTTONUP = 29
BUTTONDOWN = 31
mix = Mixer()
mix.setvolume(vol)
GPIO.setup(BUTTONUP, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTONDOWN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BUTTONUP, GPIO.FALLING, callback= lambda x: changeVolume(vol+VOLSTEP), bouncetime=100)
GPIO.add_event_detect(BUTTONDOWN, GPIO.FALLING, callback= lambda x: changeVolume(vol-VOLSTEP), bouncetime=100)
GPIO.add_event_detect(BUTTONUP, GPIO.FALLING, callback=partial(changeVolume, vol+VOLSTEP), bouncetime=100)
GPIO.add_event_detect(BUTTONDOWN, GPIO.FALLING, callback=partial(changeVolume, vol-VOLSTEP), bouncetime=100)
