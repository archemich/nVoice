import pyowm
from TextFromVoice import *
from playAudio import play_audio
owm = pyowm.OWM(API_key='639cd74b40221a097d31bc5e64e343ab', language='ru')


def get_city(data):
    
    data = data.split()
    city = data[-1]
    city = city[:-1]
    print(city)        
    #get_data 
    try:
        observation = owm.weather_at_place(city)
        w = observation.get_weather()
        temperature = int(w.get_temperature('celsius')['temp'])
        status = w.get_detailed_status()

        #play_audio
        getVoiceFromText(f'В городе {city} сейчас {temperature} градусов по Цельсию, также в {city}е  {status}.')
        play_audio()
    except:
        getVoiceFromText("Такого города не существует, повторите попытку")
        play_audio()

    
