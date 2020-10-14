import time
from threading import Timer
from playAudio import play_audio
from TextFromVoice import getVoiceFromText



class Reminder:
    def __init__(self, text=None):
        self._text = text
        self._secs = 0
        self.intro = 'Вы просили напомнить'
        if text != None:
            text.lower()
            self._text = self.parse(text)
        t = Timer(self._secs, self.remind)
        t.start()  


    def remind(self):
        if self._text == None:
            play_audio(alarm)
        else:
            getVoiceFromText(self.intro + ' ' + self._text)
            print(self.intro + ' ' + self._text)
            
    

    def parse(self, text):
        text = ''.join(text).split()
        hour = 0
        mins = 0
        secs = 0
        time_index = self.searchTime('часов', 'часа', 'час', text)

        if time_index != -1:
            hour = int(text[time_index - 1])

        time_index = self.searchTime('минут', 'минуту','минуты', text)

        if time_index != -1:
            mins = int(text[time_index - 1])

        time_index = self.searchTime('секунд', 'секунду', 'секунды', text)

        if time_index != -1:
            secs = int(text[time_index - 1])

        self._secs = hour*3600 + mins*60 + secs
        cher = text.index('через')
        
        if text[1] == 'мне':
            text = text[2:cher]
        
        else:
            text = text[1:cher]

        return ' '.join(text)

    def searchTime(self, a, b, c, text):
        try:
            time_index = text.index(a)
        except ValueError:
            try:
                time_index = text.index(b)
            except ValueError:
                try: 
                    time_index = text.index(c)
                except ValueError:
                    time_index = -1

        return time_index

