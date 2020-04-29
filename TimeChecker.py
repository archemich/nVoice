from TextFromVoice import getVoiceFromText
from playAudio import play_audio
from SupportFunkforTimeChecker import support_func
import time


def localtime():
    localtime = time.asctime( time.localtime(time.time()) )
    correct_time = localtime.split()
    correct_time = correct_time[3].split(':')

    #|----------------------------ИНСТРУКЦИЯ--------------------------------|

    #Для извлечения времени прописываем следующую строчку: 
    # "localtime()" .
    # Она все сделает сама, голос воспроизводится автоматически.
    #Для проверки стираете "#" перед строчками "correct_time[0] = 5, correct_time[1] = 16, ..."

    #|----------------------------Для проверки------------------------------|

    #       часы
    #correct_time[0] = 5

    #      минуты
    #correct_time[1] = 16

    #     секунды
    #correct_time[2] = 2

    #|-----------------------------Сама функция-----------------------------|

    #Утро

    if (int(correct_time[0]) >= 4 and int(correct_time[0]) < 13):

        if (int(correct_time[1]) == 0):
            if(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} утра.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} утра.".format(int(correct_time[0])))

        else:
            support_func(correct_time)
    #День

    elif (int(correct_time[0]) >= 13 and int(correct_time[0]) < 17):

        
        correct_time[0] = int(correct_time[0]) - 12
        if (int(correct_time[1]) == 0):
            if (int(correct_time[0]) == 1):
                getVoiceFromText(text= "Сейчас ровно час дня.")
            elif(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} часа дня.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} часов дня.".format(int(correct_time[0])))

        else: 
            support_func(correct_time)

    #Вечер

    elif (int(correct_time[0]) >= 17 and int(correct_time[0]) <= 23):

        correct_time[0] = int(correct_time[0]) - 12

        if (int(correct_time[1]) == 0):
            if(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} вечера.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} вечера.".format(int(correct_time[0])))

        else:
            support_func(correct_time)

    #Ночь

    elif (int(correct_time[0]) >= 0 and int(correct_time[0]) < 4):

        if (correct_time[0] == 0):
            correct_time[0] = 12

        if (int(correct_time[1]) == 0):
            if (int(correct_time[0]) == 1):
                getVoiceFromText(text= "Сейчас ровно час н+очи.")
            elif(int(correct_time[0]) >= 2 and int(correct_time[0]) <= 4):
                getVoiceFromText(text= "Сейчас ровно {} часа н+очи.".format(int(correct_time[0])))
            else:
                getVoiceFromText(text= "Сейчас ровно {} часов н+очи.".format(int(correct_time[0])))

        else:
            support_func(correct_time)

    play_audio()

localtime()