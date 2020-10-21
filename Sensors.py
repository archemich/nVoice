from TextFromVoice import getVoiceFromText
from playAudio import play_audio
from random import randint
import Adafruit_DHT
import smbus

sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

DEV_ADDR = 0x48
adc_channel = 0b1000010
dac_channel = 0b1000000
bus = smbus.SMBus(1)

def sensor_CO2_status():
    bus.write_byte(DEV_ADDR, adc_channel)
    bus.read_byte(DEV_ADDR)
    bus.read_byte(DEV_ADDR)
    CO2_status = bus.read_byte(DEV_ADDR)
    print(CO2_status)
    if(CO2_status < 60):
        getVoiceFromText(text = "Содержание углекислого газа в воздухе нормальное, все в порядке")
    else:
        getVoiceFromText(text = "Содержание углекислого газа в воздухе повышено, необходимо проветрить помещение")

    play_audio()
def sensor_temp_status():
    temp_status=temperature
    if(temp_status==1 or temp_status==21 or temp_status==31 or temp_status==41 or temp_status==51):
        getVoiceFromText(text = "Температура сейчас {} градус".format(int(temp_status)))
    elif(temp_status>=2 and temp_status<=4):
        getVoiceFromText(text = "Температура сейчас {} градуса".format(int(temp_status)))
    elif(temp_status>=22 and temp_status<=24):
        getVoiceFromText(text = "Температура сейчас {} градуса".format(int(temp_status)))
    elif(temp_status>=32 and temp_status<=34):
        getVoiceFromText(text = "Температура сейчас {} градуса".format(int(temp_status)))
    elif(temp_status>=42 and temp_status<=44):
        getVoiceFromText(text = "Температура сейчас {} градуса".format(int(temp_status)))
    else: 
        getVoiceFromText(text = "Температура сейчас {} градусов".format(int(temp_status)))
    play_audio()
def sensor_humidity_status():
    hum_status=humidity
    if(hum_status<=35):
        getVoiceFromText(text = "Влажность воздуха меньше тридцати пяти процентов, слишком сухо")
    elif(hum_status>35 and hum_status<=65):
        getVoiceFromText(text = "Влажность воздуха меньше шестидесяти пяти процентов, влажность оптимальна")
    elif(hum_status>65):
        getVoiceFromText(text = "Влажность воздуха ,больше шестидесяти пяти процентов, влажность высокая")
    play_audio()

def all_sensors_status():

    sensor_CO2_status()
    sensor_temp_status()
    sensor_humidity_status()

