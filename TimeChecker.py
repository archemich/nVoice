from TextFromVoice import getVoiceFromText
from playAudio import play_audio
import time



#getVoiceFromText("Местное время сейчас это %00d часа %00d минут и %00d секунд "(hour, minuts, seconds))
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time : {}".format(localtime))
