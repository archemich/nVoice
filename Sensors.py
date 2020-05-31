from TextFromVoice import getVoiceFromText
from playAudio import play_audio
from random import randint

def sensor_CO2_status():
    CO2_status=randint(200,2001)
    if(CO2_status>=300 and CO2_status<=400):
         getVoiceFromText(text = "Содержание углекислого газа в воздухе минимально и идеально для вашего здоровья")
    elif (CO2_status>400 and CO2_status<=600):
        getVoiceFromText(text = "Содержание углекислого газа в воздухе нормальное, все в порядке")
    elif (CO2_status>600 and CO2_status<=800):
        getVoiceFromText(text = "Содержание углекислого газа в воздухе немного повышено, возможно стоит проветрить помещение")
    elif (CO2_status>800 and CO2_status<=1000):
        getVoiceFromText(text = "Содержание углекислого газа в воздухе повышено, стоит проветрить помещение")
    elif (CO2_status>1000 and CO2_status<=2000):
        getVoiceFromText(text = "Содержание углекислого газа в воздухе сильно повышено, необходимо проветрить помещение")
    elif (CO2_status>2000):
        getVoiceFromText(text = "Содержание углекислого газа в воздухе опасно для здоровья, необходимо срочно проветрить помещение")
    play_audio()
def sensor_temp_status():
    temp_status=randint(0,51)
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
    hum_status=randint(0,101)
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


    
