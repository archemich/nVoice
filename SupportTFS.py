import os.path
from TheFirstSwitch import *
from TextFromVoice import getVoiceFromText

def new_name(r, index):
    check_file = os.path.exists('answer.txt')
    try:
        f = open('answer.txt', 'r')
        string = f.read()
        print('Заданное имя:')
        print(string)
        f.close()
        getVoiceFromText("Прив+ет!" + string + "снова с вами")
        play_audio()
        return string
    
    except FileNotFoundError:
        print('Заданное имя отсутствует') 
        TFS = zadanie(command(r, index), r, index).lower()
        return TFS

