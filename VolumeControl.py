from alsaaudio import Mixer
from playAudio import play_audio
from TextFromVoice import getVoiceFromText

def setVolume(text):
    text = ''.join(text).split()
    volume = int(text[text.index('на') + 1])
    print(text)
    print(volume)
    if volume >= 0 and volume <= 100:
        mix = Mixer()
        mix.setvolume(volume)
        print("поставила")
    else:
        getVoiceFromText("Нельзя поставить громкость на %s", (str(volume)))
        print("не поставила")