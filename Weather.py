from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from TextFromVoice import *
from playAudio import play_audio

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM('639cd74b40221a097d31bc5e64e343ab', config_dict)


def get_city(data):
    
    data = data.split()
    city = data[-1]
    city = city[:-1]
    print(city)    

    #get_data 
    try:
        observation = owm.weather_manager().weather_at_place(city)
        w = observation.weather
        temperature = int(w.temperature('celsius')['temp'])
        status = w.detailed_status

        #play_audio
        getVoiceFromText(f'В городе {city} сейчас {temperature} градусов по Цельсию, также в {city}е  {status}.')
        play_audio()
    except:
        getVoiceFromText("Такого города не существует, повторите попытку")
        play_audio()